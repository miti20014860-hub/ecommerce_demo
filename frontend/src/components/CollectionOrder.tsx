import { useMutation, useQueryClient } from '@tanstack/react-query';
import { createOrder } from '@/lib/fetcher';
import { useState } from 'react';
import { X } from 'lucide-react';
import type { Collection } from '@/types/type';

interface OrderModalProps {
  collection: Collection;
  onClose: () => void;
  user?: { first_name: string; last_name: string; email: string; phone?: string; paymen_methods?: string; delivery_address?: string };
}

export const OrderModal = ({ collection, onClose, user }: OrderModalProps) => {
  const queryClient = useQueryClient();

  const [formData, setFormData] = useState({
    collection: collection.name_jp,
    collection_obj: collection.id,
    first_name: user?.first_name || '',
    last_name: user?.last_name || '',
    email: user?.email || '',
    phone: user?.phone || '',
    paymen_methods: user?.paymen_methods || '',
    delivery_address: user?.delivery_address || '',
    comment: '',
  });

  const mutation = useMutation({
    mutationFn: createOrder,
    onSuccess: () => {
      alert('Order request sent successfully!');
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
    <div className="fixed inset-0 z-[100] flex items-center justify-center p-4">
      {/* Mask */}
      <div className="absolute inset-0 bg-slate-900/60 backdrop-blur-sm" onClick={onClose} />

      {/* Modal */}
      <div className="relative bg-white w-full max-w-4xl rounded-2xl shadow-2xl overflow-hidden flex flex-col max-h-[95vh]">
        <div className="flex items-center justify-between p-4 border-b">
          <h5 className="font-semibold text-lg">Order Form</h5>
          <button onClick={onClose} className="p-1 hover:bg-slate-100 rounded-full transition-colors">
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="flex-1 overflow-y-auto p-6">
          <div className="border-b-2">
            <h4 className="font-medium text-lg">Habaki Customer Policy.</h4>
            <h5 className="font-medium text-lg mt-2">A: Business Terms and Conditions</h5>
            <h6 className="block mt-2">
              (A-1) We guarantee the authenticity of every Japanese sword displayed in our online catalogue. Unless stated otherwise.*1
              *1 in case the sword is either an imitation or a copy from the original, will this be accommodated to the selling price and shown within the sword’s information.
            </h6>
            <p className="block mt-2">- Swords with the characteristics stated below are excluded.</p>
            <p className="block mt-2">- Swords which have been judged with an official certificate.</p>
            <p className="block mt-2">- Swords with a full length less than 15cm.</p>
            <p className="block mt-2">- Swords which indicate to have an inscription failure.</p>
            <p className="block mt-2">- Sword accessories; such as ornaments, brims, scabbards and etc.</p>
            <h6 className="block mt-2">
              (A-2) In a policy of this shop showing the best price from a beginning, and furthermore, we do not do a discount at all because we want to treat all customer fairly.
            </h6>
            <h6 className="block mt-2">
              (A-3) “Habaki” policy maintains a fair treatment policy for every customer on an even basis. Therefore we do not give special prize offers, discounts or other deals. Our price is already “Best Price-Quality Offer” based.
            </h6>
            <h6 className="block mt-2">
              (A-4) Once you have placed an order from our collection, until we have confirmed your payment, we will reserve the item 1 working week. (Weekends not included)
            </h6>
            <h6 className="block mt-2">
              (A-5) As soon as your payment has been confirmed, we shall apply immediately at the J.A.C.A. In case of cancellation: We are unable to cancel the application process at the J.A.C.A., since we can only terminate your order, after returning the registration documents received from the J.A.C.A. We kindly ask for your understanding.*3
            </h6>
            <p className="block mt-2">
              *3 we cannot be held responsible for any foreign laws, troubleshooting or unforeseen problems at your country’s customs, upon arrival. Doing business with us will be completely at your own choice and risk. Therefore, we strongly advise you to confirm with your country’s customs policy first, before placing an order.
            </p>
            <h6 className="block mt-2">
              (A-6) Upon exporting a “registered” sword from Japan, we will have to inform the “Japanese Agency for Cultural Affairs -(J.A.C.A.)” and apply for an “export permit for antiques”. Once the documents have been issued and attached to the sword it is usually shipped about 2 weeks later.
            </h6>
            <h6 className="block mt-2">
              (A-7) We usually use “EMS” for standard shipping, upon sending the item abroad. Shipping expenses for items with a length of more than 150cm, or items which weigh more than a “standard sword” (i.e. a spear, armour, muskets and such), will be charged an extra ￥40,000,-(JPY). A similar case applies, if Fedex is preferred over EMS. Standard shipping + insurance is included in the item’s price. *4
            </h6>
            <p className="block mt-2">
              *4 the amount of money written on the custom’s invoice also applies for the maximum insurance price in case of damage or loss. We ask for your understanding.
            </p>
            <h6 className="block mt-2">(A-8) Upon completion of delivery, we maintain a “No return or refund policy”.</h6>
            <h5 className="font-medium text-lg mt-2">B: Paymen Methods</h5>
            <h5 className="mt-2">(B-1) Wire transfer:</h5>
            <p className="block mt-2">
              We accept wire transfer to our Japanese bank or using an International postal money order. *1
            </p>
            <p className="block mt-2">
              *1 if wire transfer is chosen, we shall provide you with our banking details in our confirmation email.
            </p>
            <h5 className="mt-2">(B-2) Credit Card</h5>
            <p className="block mt-2">
              ※JCB,Visa,MasterCard,American Express,Diners Club and DISCOVER cards accepted.Currency is available only JPY.
            </p>
            <p className="block mt-2 mb-6">
              ※Credit cards other than in your name are not accepted.Please make sure to use a credit card in your own name.
            </p>
          </div>

          <form onSubmit={handleSubmit} className="mt-4 space-y-4">
            {/* Title */}
            <div className="mb-4">
              <label className="block text-lg text-slate-900 text-center">{collection.name_jp}</label>
              <label className="block font-medium text-slate-900 text-center">{collection.name_en}</label>
            </div>

            {/* Input */}
            <div className="grid grid-cols-2 gap-4">
              <div className="space-y-1">
                <label className="text-xs font-medium text-slate-500 uppercase">First name</label>
                <input
                  required
                  type="text"
                  name="first_name"
                  placeholder="Fist name"
                  value={formData.first_name}
                  onChange={handleChange}
                  className="w-full border border-slate-300 rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all"
                />
              </div>

              <div className="space-y-1">
                <label className="text-xs font-medium text-slate-500 uppercase">Last name</label>
                <input
                  required
                  type="text"
                  name="last_name"
                  placeholder="Last name"
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
                placeholder="Email address"
                value={formData.email}
                onChange={handleChange}
                className="w-full border border-slate-300 rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all"
              />
            </div>

            <div className="space-y-1">
              <label className="text-xs font-medium text-slate-500 uppercase">Phone Number</label>
              <input
                required
                type="text"
                name="phone"
                placeholder="Phone number"
                value={formData.phone}
                onChange={handleChange}
                className="w-full border border-slate-300 rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all"
              />
            </div>

            <div className="space-y-1">
              <label className="text-xs font-medium text-slate-500 uppercase">Paymen Method</label>
              <input
                required
                type="text"
                name="paymen_methods"
                placeholder="Method and bank name"
                value={formData.paymen_methods}
                onChange={handleChange}
                className="w-full border border-slate-300 rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all"
              />
            </div>

            <div className="mb-2 space-y-1">
              <label className="text-xs font-medium text-slate-500 uppercase">Delivery Address</label>
              <textarea
                required
                name="delivery_address"
                rows={2}
                placeholder="Country and delivery address"
                value={formData.delivery_address}
                onChange={handleChange}
                className="w-full border border-slate-300 rounded-lg p-2.5 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all"
              />
            </div>

            <div className="mt-0 space-y-1">
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
              ${mutation.isPending ? 'bg-slate-400' : 'bg-black hover:bg-slate-800 active:scale-[0.98]'}`}
            >
              {mutation.isPending ? 'Submitting...' : 'Submit'}
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default OrderModal