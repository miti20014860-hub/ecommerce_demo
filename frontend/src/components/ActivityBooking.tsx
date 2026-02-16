import { useMutation, useQueryClient } from '@tanstack/react-query';
import { createBooking } from '@/lib/fetcher';
import { useState } from 'react';
import { X } from 'lucide-react';
import type { Activity } from '@/types/type';

interface BookingModalProps {
  activity: Activity;
  onClose: () => void;
  user?: { first_name: string; last_name: string; email: string; phone?: string };
}

export const BookingModal = ({ activity, onClose, user }: BookingModalProps) => {
  const queryClient = useQueryClient();

  const [formData, setFormData] = useState({
    activity: activity.title,
    activity_obj: activity.id,
    first_name: user?.first_name || '',
    last_name: user?.last_name || '',
    email: user?.email || '',
    phone: user?.phone || '',
    prefer_date: '',
    comment: '',
  });

  const mutation = useMutation({
    mutationFn: createBooking,
    onSuccess: () => {
      alert('Booking request sent successfully!');
      queryClient.invalidateQueries({ queryKey: ['bookings'] });
      onClose();
    },
    onError: (error: Error) => {
      alert(error.message);
    }
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    mutation.mutate(formData);
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { name, value } = e.target;
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  return (
    <div className="fixed inset-0 z-[1000] flex items-center justify-center p-4">
      {/* Mask */}
      <div className="absolute inset-0 bg-slate-900/60 backdrop-blur-sm" onClick={onClose} />

      {/* Modal */}
      <div className="relative bg-white w-full max-w-xl rounded-2xl shadow-2xl overflow-hidden">
        <div className="flex items-center justify-between p-4 border-b">
          <h5 className="font-semibold text-lg">Booking Form</h5>
          <button onClick={onClose} className="p-1 hover:bg-slate-100 rounded-full transition-colors">
            <X className="w-5 h-5" />
          </button>
        </div>

        <form onSubmit={handleSubmit} className="p-6 space-y-4 max-h-[80vh] overflow-y-auto">
          {/* Title */}
          <div className="mb-4">
            <label className="block font-semibold text-slate-900">{activity.title}</label>
          </div>

          {/* Input */}
          <div className="grid grid-cols-2 gap-4">
            <div className="space-y-1">
              <label className="text-xs font-medium text-slate-500 uppercase">First name</label>
              <input
                required
                name="first_name"
                value={formData.first_name}
                onChange={handleChange}
                className="w-full border border-slate-300 rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all"
              />
            </div>
            <div className="space-y-1">
              <label className="text-xs font-medium text-slate-500 uppercase">Last name</label>
              <input
                required
                name="last_name"
                value={formData.last_name}
                onChange={handleChange}
                className="w-full border border-slate-300 rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all"
              />
            </div>
          </div>

          <div className="space-y-1">
            <label className="text-xs font-medium text-slate-500 uppercase">Email Address</label>
            <input
              required
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              className="w-full border border-slate-300 rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all"
            />
          </div>

          <div className="space-y-1">
            <label className="text-xs font-medium text-slate-500 uppercase">Phone Number</label>
            <input
              type="text"
              name="phone"
              placeholder="Optional"
              value={formData.phone}
              onChange={handleChange}
              className="w-full border border-slate-300 rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all"
            />
          </div>

          <div className="space-y-1">
            <label className="text-xs font-medium text-slate-500 uppercase">Preferred Date</label>
            <input
              required
              type="date"
              name="prefer_date"
              value={formData.prefer_date}
              onChange={handleChange}
              className="w-full border border-slate-300 rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all"
            />
          </div>

          <div className="space-y-1">
            <label className="text-xs font-medium text-slate-500 uppercase">Comment</label>
            <textarea
              name="comment"
              rows={4}
              placeholder="Optional"
              value={formData.comment}
              onChange={handleChange}
              className="w-full border border-slate-300 rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all"
            />
          </div>

          {/* Submit */}
          <button
            type="submit"
            disabled={mutation.isPending}
            className={`w-full py-3 rounded-xl font-semibold text-white transition-all shadow-lg
              ${mutation.isPending ? 'bg-slate-400' : 'bg-black hover:bg-slate-800 active:scale-[0.98]'}
            `}
          >
            {mutation.isPending ? 'Submitting...' : 'Submit'}
          </button>
        </form>
      </div>
    </div>
  );
};

export default BookingModal