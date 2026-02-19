import { useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import { fetchMemberProfile, signOut } from '@/lib/fetcher';
import { UpdateProfileForm } from '@/components/member/UpdateProfileForm';

type TabType = 'home' | 'profile' | 'bookings' | 'orders';

export const Account = () => {
  const [activeTab, setActiveTab] = useState<TabType>('home');

  const { data: user, isLoading } = useQuery({
    queryKey: ['profile'],
    queryFn: fetchMemberProfile,
  });


  if (isLoading) return <div className='text-center py-20'>Loading...</div>;
  if (!user) return <div className='text-center py-20 text-slate-500'>Please sign in to view this page.</div>;

  return (
    <div className='container mx-auto md:px-16 lg:px-32 xl:px-64 2xl:px-96'>
      <div className='bg-slate-100'>

        {/* Tab Navigation */}
        <div className='flex sm:text-lg'>
          {(['home', 'profile', 'bookings', 'orders'] as TabType[]).map((tab) => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`flex-1 py-3 font-medium transition-colors uppercase tracking-wider
                ${activeTab === tab ? 'bg-gray-700 text-white' : 'bg-slate-50 text-slate-600 hover:bg-slate-200'}
              `}
            >
              {tab}
            </button>
          ))}
        </div>

        {/* Tab Content */}
        <div className=''>

          {/* HOME TAB */}
          {activeTab === 'home' && (
            <div className='min-h-[50vh] flex flex-col'>
              <div className='text-center my-auto'>
                <h3 className='text-4xl font-serif mb-5'>{user.username}</h3>
                <h3 className='text-2xl text-slate-500'>Welcome Back</h3>
              </div>
              <button
                onClick={() => signOut()}
                className='w-full bg-black text-white py-4 font-medium hover:bg-slate-800'
              >
                SIGN OUT
              </button>
            </div>
          )}

          {/* PROFILE TAB */}
          {activeTab === 'profile' && (
            <div className=''>
              <div className=''>
                <UpdateProfileForm
                  user={user}
                />
              </div>
            </div>
          )}

          {/* BOOKINGS TAB */}
          {activeTab === 'bookings' && (
            <div className='min-h-[50vh] text-sm sm:text-base'>
              {user.bookings && user.bookings.length > 0 ? (
                <div className='text-center'>
                  <div className="bg-slate-800 text-white grid grid-cols-16 font-medium uppercase">
                    <p className="col-span-1 p-4">ID</p>
                    <p className="col-span-9 p-4">Activity</p>
                    <p className="col-span-3 p-4">Date</p>
                    <p className="col-span-3 p-4">Status</p>
                  </div>

                  {user.bookings.map((booking) => (
                    <div key={booking.id} className='bg-slate-200 grid grid-cols-16 font-medium hover:bg-slate-50'>
                      <p className='col-span-1 py-3 font-medium'>#{booking.id}</p>
                      <div className='col-span-9 py-3'>
                        <a href={`/activity/${booking.activity_obj.id}`} className='hover:underline line-clamp-1'>
                          {booking.activity_obj.title}
                        </a>
                      </div>
                      <p className='col-span-3 py-3'>{new Date(booking.prefer_date).toLocaleDateString()}</p>
                      <div className='col-span-3 py-3'>
                        <span className='bg-green-100 text-green-700 px-1 py-1 text-xs font-medium rounded-full'>
                          SUBMITTED
                        </span>
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <EmptyState message="You haven't booked any activity yet." link='/activity' linkText='Explore Activity' />
              )}
            </div>
          )}

          {/* ORDERS TAB */}
          {activeTab === 'orders' && (
            <div className='min-h-[50vh] text-sm sm:text-base'>
              {user.orders && user.orders.length > 0 ? (
                <div className='text-center md:text-md'>
                  <div className="bg-slate-800 text-white grid grid-cols-16 font-medium uppercase">
                    <p className="col-span-1 p-4">ID</p>
                    <p className="col-span-9 p-4">Collection</p>
                    <p className="col-span-3 p-4">Price</p>
                    <p className="col-span-3 p-4">Status</p>
                  </div>

                  {user.orders.map((order) => (
                    <div key={order.id} className='bg-slate-200 grid grid-cols-16 font-medium hover:bg-slate-50'>
                      <p className='col-span-1 py-3 font-medium'>#{order.id}</p>
                      <div className='col-span-9 py-3'>
                        <a href={`/collection/${order.collection_obj.id}`} className='hover:underline line-clamp-1'>
                          {order.collection_obj.name_jp}

                        </a>
                      </div>
                      <p className='col-span-3 py-3 line-clamp-1 '>{Number(order.collection_obj.price).toLocaleString()} {order.collection_obj.currency}</p>
                      <div className='col-span-3 py-3'>
                        <span className='bg-green-100 text-green-700 px-1 py-1 text-xs font-medium rounded-full'>
                          SUBMITTED
                        </span>
                      </div>
                    </div>

                  ))}
                </div>
              ) : (
                <EmptyState message="You haven't placed any orders yet." link='/collection' linkText='Explore Collection' />
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

const EmptyState = ({ message, link, linkText }: { message: string, link: string, linkText: string }) => (
  <div className='text-center py-20 bg-slate-100'>
    <p className='text-slate-500 mb-4'>{message}</p>
    <a href={link} className='inline-block border border-slate-400 px-6 py-2 text-slate-600 hover:bg-white transition-colors'>
      {linkText}
    </a>
  </div>
);

export default Account
