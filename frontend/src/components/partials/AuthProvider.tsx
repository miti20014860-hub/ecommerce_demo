import { useState, useEffect } from 'react';
import { useQuery, useQueryClient } from '@tanstack/react-query';
import { AuthContext } from '@/lib/auth-context';
import { fetchMemberProfile } from '@/lib/fetcher';

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {

  const [token, setToken] = useState<string | null>(() => {
    const savedToken = localStorage.getItem('access_token');
    return (savedToken && savedToken !== 'undefined') ? savedToken : null;
  });

  const queryClient = useQueryClient();

  const { data: user, isLoading, error, refetch } = useQuery({
    queryKey: ['profile'],
    queryFn: fetchMemberProfile,
    enabled: !!token,
    retry: false,
    gcTime: 1000 * 60 * 30,
  });

  useEffect(() => {
    if (error) {
      localStorage.removeItem('access_token');
      localStorage.removeItem('refresh_token');
      queryClient.removeQueries({ queryKey: ['profile'] });
    }
  }, [error, queryClient]);

  useEffect(() => {
    const handleStorageChange = () => {
      const currentToken = localStorage.getItem('access_token');
      if (!currentToken && token) {
        setToken(null);
        queryClient.clear();
      }
    };
    window.addEventListener('storage', handleStorageChange);
    return () => window.removeEventListener('storage', handleStorageChange);
  }, [queryClient, token]);

  const login = (access: string, refresh: string) => {
    localStorage.setItem('access_token', access);
    localStorage.setItem('refresh_token', refresh);
    setToken(access);
    refetch();
  };

  const logout = () => {
    localStorage.clear();
    setToken(null);
    queryClient.clear();
    window.location.href = '/login';
  };

  const value = {
    user: user || null,
    isAuthenticated: !!token && !!user,
    isLoading,
    login,
    logout,
  };


  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};

export default AuthProvider