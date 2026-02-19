import { createContext, useContext } from 'react';
import type { MemberProfile } from '@/types/type';

interface AuthContextType {
  user: MemberProfile | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  login: (access: string, refresh: string) => void;
  logout: () => void;
}

export const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) throw new Error('useAuth must be used within AuthProvider');
  return context;
};