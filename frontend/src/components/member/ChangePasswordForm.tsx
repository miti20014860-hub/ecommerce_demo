import { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import { changePassword, signOut } from '@/lib/fetcher';

export const ChangePasswordForm = () => {
  const changePasswordMutation = useMutation({
    mutationFn: changePassword,
    onSuccess: () => {
      alert('Password changed! Please log in again.');
      signOut();
    },
    onError: (error) => { alert(error.message); }
  });

  const [passwordData, setPasswordData] = useState({
    old_password: '',
    new_password: '',
    confirm_password: '',
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (passwordData.new_password !== passwordData.confirm_password) {
      alert('New passwords do not match!');
      return;
    }

    changePasswordMutation.mutate({
      old_password: passwordData.old_password,
      new_password: passwordData.new_password,
      confirm_password: passwordData.confirm_password,
    });
  };

  return (
    <form className='flex flex-col px-4'>
      <p className='mt-3 ms-1 text-lg font-semibold'>Enter password to confirm identity</p>
      <input
        required
        type='password'
        name='old_password'
        placeholder='Current Password'
        value={passwordData.old_password}
        onChange={(e) => setPasswordData({ ...passwordData, old_password: e.target.value })}
        className='bg-white border border-slate-300 p-2 mt-3 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all'
      />
      <input
        required
        type='password'
        name='new_password'
        placeholder='New Password'
        value={passwordData.new_password}
        onChange={(e) => setPasswordData({ ...passwordData, new_password: e.target.value })}
        className='bg-white border border-slate-300 p-2 mt-2 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all'
      />
      <input
        required
        type='password'
        name='confirm_password'
        placeholder='Confirm New Password'
        value={passwordData.confirm_password}
        onChange={(e) => setPasswordData({ ...passwordData, confirm_password: e.target.value })}
        className='bg-white border border-slate-300 p-2 mt-2 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all'
      />
      <button
        onClick={handleSubmit}
        disabled={changePasswordMutation.isPending}
        className='bg-black text-white py-3 hover:bg-gray-800 disabled:bg-gray-400 mt-3'
      >
        {changePasswordMutation.isPending ? 'Changing...' : 'Confirm Password Change'}
      </button>

    </form>
  );
};