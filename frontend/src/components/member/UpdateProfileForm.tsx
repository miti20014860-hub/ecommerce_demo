import { useState } from 'react';
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { updateProfile } from '@/lib/fetcher';
import { ChangePasswordForm } from '@/components/member/ChangePasswordForm';
import type { MemberProfile } from '@/types/type';

export const UpdateProfileForm = ({ user }: { user: MemberProfile }) => {
  const queryClient = useQueryClient();

  const [isUpdateProfileOpen, setUpdateProfileOpen] = useState(false);
  const [isChangePasswordOpen, setChangePasswordOpen] = useState(false);

  const handleToggleUpdate = () => {
    setUpdateProfileOpen(!isUpdateProfileOpen);
    setChangePasswordOpen(false);
  };
  const handleTogglePassword = () => {
    setChangePasswordOpen(!isChangePasswordOpen);
    setUpdateProfileOpen(false);
  };

  const updateProfileMutation = useMutation({
    mutationFn: updateProfile,
    onSuccess: () => {
      alert("Profile updated successfully!");
      setUpdateProfileOpen(false);
      setFormData(prev => ({ ...prev, password: '' }));
      queryClient.invalidateQueries({ queryKey: ['profile'] });
    },
    onError: () => {
      alert('Password is incorrect. Identity verification failed');
    }
  });

  const [formData, setFormData] = useState({
    first_name: user?.first_name || '',
    last_name: user?.last_name || '',
    email: user?.email || '',
    phone: user?.phone || '',
    payment: user?.payment || '',
    address: user?.address || '',
    password: ''
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    updateProfileMutation.mutate(formData);
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  return (
    <form className="min-h-[50vh] flex flex-col">
      <div className={`grid transition-all duration-500 ease-in-out ${isUpdateProfileOpen
        ? 'grid-rows-[1fr] opacity-100'
        : 'grid-rows-[0fr] opacity-0'
        }`}>
        <div className="overflow-hidden flex flex-col px-4">
          <p className="mt-3 ms-1 text-lg font-semibold">Enter password to confirm identity</p>
          <input
            required
            type='password'
            name='password'
            placeholder='Password'
            value={formData.password}
            onChange={handleChange}
            className='bg-white border border-slate-300 p-2 mt-3 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all'
          />
          <button
            type="submit"
            onClick={handleSubmit}
            disabled={updateProfileMutation.isPending}
            className="bg-black text-white py-3 hover:bg-gray-800 disabled:bg-gray-400 mt-3"
          >
            {updateProfileMutation.isPending ? 'Saving...' : 'Confirm Profile Change'}
          </button>
        </div>
      </div>
      <div className={`grid transition-all duration-500 ease-in-out ${isChangePasswordOpen
        ? 'grid-rows-[1fr] opacity-100'
        : 'grid-rows-[0fr] opacity-0'
        }`}>
        <div className="overflow-hidden">
          <ChangePasswordForm />
        </div>
      </div>
      <div className='grid grid-cols-3 px-5 items-center mt-3 border-b border-white'>
        <label className='col-span-1 font-medium text-slate-700'>Fist name</label>
        <input
          type='text'
          name='first_name'
          placeholder='First name'
          value={formData.first_name}
          onChange={handleChange}
          className='col-span-2 bg-white border border-slate-300 rounded-lg p-2 mb-1 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all'
        />
      </div>
      <div className='flex grid grid-cols-3 px-5 items-center mt-1 border-b border-white'>
        <label className='col-span-1 font-medium text-slate-700'>Last name</label>
        <input
          type='text'
          name='last_name'
          placeholder='Last name'
          value={formData.last_name}
          onChange={handleChange}
          className='col-span-2 bg-white border border-slate-300 rounded-lg p-2 mb-1 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all'
        />
      </div>
      <div className='flex grid grid-cols-3 px-5 items-center mt-1 border-b border-white'>
        <label className='col-span-1 font-medium text-slate-700'>Email address</label>
        <input
          readOnly
          type='email'
          name='email'
          placeholder='Email address'
          value={formData.email}
          onChange={handleChange}
          className='col-span-2 bg-white border border-slate-300 rounded-lg p-2 mb-1 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all'
        />
      </div>
      <div className='flex grid grid-cols-3 px-5 items-center mt-1 border-b border-white'>
        <label className='col-span-1 font-medium text-slate-700'>Phone number</label>
        <input
          type='tel'
          name='phone'
          placeholder='Phone number'
          value={formData.phone}
          onChange={handleChange}
          className='col-span-2 bg-white border border-slate-300 rounded-lg p-2 mb-1 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all'
        />
      </div>
      <div className='flex grid grid-cols-3 px-5 items-center mt-1 border-b border-white'>
        <label className='col-span-1 font-medium text-slate-700'>Payment method</label>
        <input
          type='text'
          name='payment'
          placeholder='Method and bank name'
          value={formData.payment}
          onChange={handleChange}
          className='col-span-2 bg-white border border-slate-300 rounded-lg p-2 mb-1 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all'
        />
      </div>

      <div className='flex grid grid-cols-3 px-5 items-center mt-1 border-b border-white'>
        <label className='col-span-1 font-medium text-slate-700'>Delivery Address</label>
        <textarea
          rows={1}
          name='address'
          placeholder='Country and delivery address'
          value={formData.address}
          onChange={handleChange}
          className='col-span-2 bg-white border border-slate-300 rounded-lg p-2 mb-1 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all'
        />
      </div>


      <div className="grid grid-cols-2 mt-auto">
        <button
          type="button"
          onClick={handleToggleUpdate}
          className="col-span-1 bg-sky-600 text-white py-3 font-bold hover:bg-sky-700"
        >
          Update Profile
        </button>
        <button
          type="button"
          onClick={handleTogglePassword}
          className="col-span-1 bg-rose-600 text-white py-3 font-bold hover:bg-rose-700"
        >
          Change Password
        </button>
      </div>
    </form>
  );
};