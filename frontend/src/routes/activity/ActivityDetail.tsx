import { useParams } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import { useState } from 'react';
import { fetchActivityById, fetchMemberProfile } from '@/lib/fetcher';
import { ChevronLeft, ChevronRight, UserCheck, Users, Clock } from 'lucide-react';
import BookingModal from '@/components/activity/ActivityBooking';
import Map from '@/components/partials/Map';
import type { Activity } from '@/types/type';

export const ActivityDetail = () => {
  const { id } = useParams<{ id: string }>();
  const { data: activity, isLoading, isError, error } = useQuery({
    queryKey: ['activity', id],
    queryFn: () => fetchActivityById(Number(id)),
    enabled: !!id,
  });

  const token = localStorage.getItem('access_token');
  const { data: user } = useQuery({
    queryKey: ['profile'],
    queryFn: fetchMemberProfile,
    enabled: !!token
  });

  const [currentImg, setCurrentImg] = useState(0);
  const [isLightboxOpen, setIsLightboxOpen] = useState(false);
  const [isBookingModalOpen, setIsBookingModalOpen] = useState(false);

  const imagesLength = activity?.images.length ?? 0;
  const nextImg = () => { if (imagesLength === 0) return; setCurrentImg((prev) => (prev + 1) % imagesLength); }
  const prevImg = () => { if (imagesLength === 0) return; setCurrentImg((prev) => (prev - 1 + imagesLength) % imagesLength); }

  if (isLoading) { return <div className='text-center py-20'>Loading...</div>; }
  if (isError || !activity) { return <div className='text-center py-20'>Loading failed: {error?.message}</div>; }

  return (
    <main className='container mx-auto lg:px-16 xl:px-32 2xl:px-64 px-2'>

      {/* Carousel */}
      <div className='relative aspect-[21/9] overflow-hidden bg-slate-100 group'>
        <img
          src={activity.images[currentImg].image}
          alt={activity.images[currentImg]?.caption || 'Image'}
          className='w-full h-full object-cover cursor-zoom-in'
          onClick={() => setIsLightboxOpen(true)}
        />
        {imagesLength > 1 && (
          <div className='text-white'>
            <button onClick={prevImg} className='absolute left-4 top-1/2 -translate-y-1/2 bg-black/30 hover:bg-black/50 p-2 rounded-full opacity-0 group-hover:opacity-100 transition-opacity'>
              <ChevronLeft />
            </button>
            <button onClick={nextImg} className='absolute right-4 top-1/2 -translate-y-1/2 bg-black/30 hover:bg-black/50 p-2 rounded-full opacity-0 group-hover:opacity-100 transition-opacity'>
              <ChevronRight />
            </button>
          </div>
        )}
      </div>

      <div className='grid grid-cols-1 lg:grid-cols-12 gap-5'>
        {/* Left */}
        <div className='lg:col-span-8'>
          {/* Title */}
          <div className='mt-3'>
            <h3 className='text-2xl xl:text-3xl font-serif'>{activity.title}</h3>
            <div className='flex gap-4 items-center text-slate-800 mt-2'>
              <span className='underline decoration-slate-800'>{activity.provider}</span>
              <span>/</span>
              <span className='underline font-medium decoration-slate-800'>{activity.type_display}</span>
            </div>
          </div>

          {/* Card */}
          <div className='grid grid-cols-3 mt-5'>
            <div className='border border-slate-200 p-2 rounded-lg flex flex-col items-center text-center'>
              <Users className='w-5 h-5 text-slate-700 mb-1' />
              <span className='text-xs text-slate-700 uppercase'>Participants</span>
              <span className='font-medium text-sm'>{activity.participants}</span>
            </div>
            <div className='border border-slate-200 p-2 rounded-lg flex flex-col items-center text-center'>
              <UserCheck className='w-5 h-5 text-slate-700 mb-1' />
              <span className='text-xs text-slate-700 uppercase'>Target Age</span>
              <span className='font-medium text-sm'>{activity.target_age}</span>
            </div>
            <div className='border border-slate-200 p-2 rounded-lg flex flex-col items-center text-center'>
              <Clock className='w-5 h-5 text-slate-700 mb-1' />
              <span className='text-xs text-slate-700 uppercase'>Duration</span>
              <span className='font-medium text-sm'>{activity.duration}</span>
            </div>
          </div>

          {/* Plan */}
          <div className='mt-5'>
            <h2 className='text-2xl font-medium mb-3 underline'>Plan Description</h2>
            <div className='max-w-none text-slate-600 whitespace-pre-line'>
              {activity.description}
            </div>

            <div className='space-y-6 my-4'>
              {[1, 2, 3].map((num) => {
                const planTitle = activity[`plan_${num}` as keyof Activity];
                if (!planTitle) return null;
                return (
                  <div key={num} className=''>
                    <div className='flex justify-between font-medium items-baseline'>
                      <h3 className='text-lg'>{String(planTitle)}</h3>
                      <div>
                        <span className='text-lg me-1'>{Number(activity[`price_${num}` as keyof Activity]).toLocaleString()}</span>
                        <span>{activity.currency}</span>
                      </div>
                    </div>
                    <p className='text-slate-600 mt-1'>
                      {String(activity[`summary_${num}` as keyof Activity])}
                    </p>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Information */}
          <div className='mt-5 '>
            <h3 className='text-2xl font-medium bg-slate-50 p-2 border-l-4 border-slate-500 mb-3'>More Information</h3>
            <h4 className='text-lg font-medium ms-1 mb-3'>Reservation Instructions</h4>
            <div className='grid gap-y-1 text-md'>
              <div className='flex'><span className='w-40 bg-slate-50 p-1'>Participants</span><span className='p-1'>{activity.min_p}</span></div>
              <div className='flex'><span className='w-40 bg-slate-50 p-1'>Min. participants</span><span className='p-1'>{activity.participants}</span></div>
              <div className='flex'><span className='w-40 bg-slate-50 p-1'>Event Ends</span><span className='p-1'>{activity.event_ends}</span></div>
              <div className='flex'><span className='w-40 bg-slate-50 p-1'>Reg. Deadline</span><span className='p-1'>{activity.reg_deadline}</span></div>
            </div>
          </div>
          <div className='mt-4'>
            <h4 className='text-lg font-medium p-1'>Address</h4>
            <p className='bg-slate-50 mt-1 p-1'>{activity.address}</p>
          </div>

          {/* Map */}
          {activity.lat && activity.lng && (
            <section className='mt-4'>
              <Map
                lat={activity.lat}
                lng={activity.lng}
                address={activity.address}
                zoom={15}
                height='400px'
              />
            </section>
          )}
        </div>

        {/* Right */}
        <div className='lg:col-span-4'>
          <div className='sticky top-6 border border-slate-200 rounded-xl p-5 shadow-sm bg-white lg:mt-4'>
            <p className='text-slate-600 mb-1'>{activity.fee_details}</p>
            <div className='flex items-baseline mb-2'>
              {activity.minimum_charge === '0' ? (
                <span className='text-3xl font-medium'>Free</span>
              ) : (
                <div className='font-medium'>
                  <span className='text-3xl me-1'>{Number(activity.minimum_charge).toLocaleString()}</span>
                  <span className='text-xl'>{activity.currency} ~ (with tax)</span>
                </div>
              )}
            </div>

            <div className='bg-slate-50/50 rounded-lg text-sm mb-6'>
              <p className='text-slate-600 mb-1'>Included in price:</p>
              <p className='text-slate-600'>{activity.price_included}</p>
            </div>

            {activity.is_appointment === 'yes' && (
              <button
                onClick={() => setIsBookingModalOpen(true)}
                className='w-full bg-rose-600 hover:bg-rose-500 text-white font-bold py-2 rounded-lg transition-colors cursor-pointer'
              >
                Book
              </button>
            )}
          </div>
        </div>
      </div>

      {/* Lightbox */}
      {isLightboxOpen && (
        <div
          onClick={() => setIsLightboxOpen(false)}
          className="fixed inset-0 z-[1000] flex justify-center items-center bg-black/70"
        >
          <div onClick={(e) => e.stopPropagation()} className="relative group cursor-default">
            <img
              src={activity.images[currentImg].image}
              alt={activity.images[currentImg]?.caption || 'Enlarged view'}
              className="max-w-[90vw] max-h-[90vh] object-contain"
            />

            <div className="absolute -bottom-10 left-1/2 -translate-x-1/2 text-white/70 text-sm">
              {currentImg + 1} / {imagesLength}
            </div>

            {imagesLength > 1 && (
              <div className="text-white">
                <button onClick={prevImg} className="absolute left-4 top-1/2 -translate-y-1/2 bg-black/20 hover:bg-black/50 p-2 rounded-full opacity-0 group-hover:opacity-100 transition-opacity">
                  <ChevronLeft />
                </button>
                <button onClick={nextImg} className="absolute right-4 top-1/2 -translate-y-1/2 bg-black/20 hover:bg-black/50 p-2 rounded-full opacity-0 group-hover:opacity-100 transition-opacity">
                  <ChevronRight />
                </button>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Booking */}
      {isBookingModalOpen && (
        <BookingModal
          activity={activity}
          user={user}
          onClose={() => setIsBookingModalOpen(false)}
        />
      )}
    </main >
  )
}
export default ActivityDetail
