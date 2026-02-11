import { useParams } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import { useState } from 'react';
import { formatDate } from '@/utils/formatTime';
import { fetchActivityById } from '@/lib/fetcher';
import { ChevronLeft, ChevronRight, X, Calendar, Users, Clock } from 'lucide-react';
import type { Activity } from '@/types/type';

export const Plan = () => {
  const { id } = useParams<{ id: string }>();
  const { data: activity, isLoading, isError, error } = useQuery({
    queryKey: ['activity', id],
    queryFn: () => fetchActivityById(Number(id)),
    enabled: !!id,
  });

  const [currentImg, setCurrentImg] = useState(0);
  const [isLightboxOpen, setIsLightboxOpen] = useState(false);
  // const [isBookingModalOpen, setIsBookingModalOpen] = useState(false);

  const images = (activity?.images && activity.images.length > 0)
    ? activity.images
    : [{ image: '/img/cover21_9.jpg' }];

  const nextImg = () => setCurrentImg((prev) => (prev + 1) % images.length);
  const prevImg = () => setCurrentImg((prev) => (prev - 1 + images.length) % images.length);

  if (isLoading) { return <div className='text-center py-20'>Loading...</div>; }
  if (isError || !activity) { return <div className='text-center py-20'>Loading failed: {error?.message}</div>; }

  return (
    <main className='container mx-auto lg:px-8 xl:px-16 2xl:px-24'>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">

          {/* 左側主要內容 (col-lg-8) */}
          <div className="lg:col-span-8">

            {/* Carousel 區域 */}
            <div className="relative aspect-[21/9] overflow-hidden rounded-xl bg-slate-100 group">
              <img
                src={images[currentImg].image}
                alt={activity.title}
                className="w-full h-full object-cover cursor-zoom-in"
                onClick={() => setIsLightboxOpen(true)}
              />
              {images.length > 1 && (
                <>
                  <button onClick={prevImg} className="absolute left-4 top-1/2 -translate-y-1/2 bg-black/30 hover:bg-black/50 text-white p-2 rounded-full opacity-0 group-hover:opacity-100 transition-opacity">
                    <ChevronLeft />
                  </button>
                  <button onClick={nextImg} className="absolute right-4 top-1/2 -translate-y-1/2 bg-black/30 hover:bg-black/50 text-white p-2 rounded-full opacity-0 group-hover:opacity-100 transition-opacity">
                    <ChevronRight />
                  </button>
                </>
              )}
            </div>

            {/* 標題與基本資訊 */}
            <div className="mt-6">
              <h1 className="text-3xl font-bold text-slate-900">{activity.title}</h1>
              <div className="flex gap-4 mt-3 text-slate-600 items-center">
                <span className="underline decoration-slate-300">{activity.provider}</span>
                <span>/</span>
                <span className="underline decoration-slate-300">{activity.type_display}</span>
              </div>
            </div>

            {/* 核心規格卡片 */}
            <div className="grid grid-cols-3 gap-4 mt-6">
              <div className="border border-slate-200 p-4 rounded-lg flex flex-col items-center text-center">
                <Users className="w-5 h-5 text-blue-500 mb-1" />
                <span className="text-xs text-slate-400 uppercase">Participants</span>
                <span className="font-semibold text-sm">{activity.participants}</span>
              </div>
              <div className="border border-slate-200 p-4 rounded-lg flex flex-col items-center text-center">
                <Calendar className="w-5 h-5 text-blue-500 mb-1" />
                <span className="text-xs text-slate-400 uppercase">Min Age</span>
                <span className="font-semibold text-sm">{activity.participating_age}</span>
              </div>
              <div className="border border-slate-200 p-4 rounded-lg flex flex-col items-center text-center">
                <Clock className="w-5 h-5 text-blue-500 mb-1" />
                <span className="text-xs text-slate-400 uppercase">Duration</span>
                <span className="font-semibold text-sm">{activity.duration}</span>
              </div>
            </div>

            {/* 方案詳情 */}
            <div className="mt-10">
              <h2 className="text-xl font-bold border-b pb-2 mb-4">Plan Description</h2>
              <div className="prose prose-slate max-w-none text-slate-600 whitespace-pre-line">
                {activity.description}
              </div>

              {/* 多個方案清單 */}
              <div className="space-y-6 mt-8">
                {[1, 2, 3].map((num) => {
                  const planTitle = activity[`plan_${num}` as keyof Activity];
                  if (!planTitle) return null;
                  return (
                    <div key={num} className="bg-slate-50 p-4 rounded-lg border-l-4 border-blue-500">
                      <div className="flex justify-between items-baseline">
                        <h3 className="font-bold text-lg">{String(planTitle)}</h3>
                        <span className="text-blue-600 font-bold">
                          {String(activity[`price_${num}` as keyof Activity])} JPY
                        </span>
                      </div>
                      <p className="text-slate-500 text-sm mt-1">
                        {String(activity[`summary_${num}` as keyof Activity])}
                      </p>
                    </div>
                  );
                })}
              </div>
            </div>

            {/* 更多資訊表格 */}
            <div className="mt-12">
              <h2 className="text-xl font-bold bg-slate-100 p-3 border-l-4 border-slate-800 mb-6">More Information</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-y-4 text-sm">
                <div className="flex border-b pb-2"><span className="w-40 text-slate-400">Min. participants</span><span>{activity.min_p}</span></div>
                <div className="flex border-b pb-2"><span className="w-40 text-slate-400">Registration Deadline</span><span>{activity.reg_deadline}</span></div>
                <div className="flex border-b pb-2"><span className="w-40 text-slate-400">Event Ends</span><span>{activity.event_ends}</span></div>
                <div className="flex border-b pb-2"><span className="w-40 text-slate-400">Address</span><span>{activity.address}</span></div>
              </div>
            </div>
          </div>

          {/* 右側側邊欄 (col-lg-4) */}
          <div className="lg:col-span-4">
            <div className="sticky top-6 border border-slate-200 rounded-xl p-6 shadow-sm bg-white">
              <p className="text-slate-400 text-sm mb-2">{activity.fee_details}</p>
              <div className="flex items-baseline gap-2 mb-4">
                {activity.minimum_charge === '0' ? (
                  <span className="text-3xl font-bold">Free</span>
                ) : (
                  <>
                    <span className="text-3xl font-bold text-slate-900">{activity.minimum_charge.toLocaleString()}</span>
                    <span className="text-sm text-slate-500">{activity.minimum_charge} ~ (with tax)</span>
                  </>
                )}
              </div>

              <div className="bg-slate-50 p-3 rounded-lg text-xs text-slate-500 mb-6">
                <strong className="block text-slate-700 mb-1">Included in price:</strong>
                {activity.price_included}
              </div>

              {activity.is_appointment === 'yes' && (
                <button
                  // onClick={() => setIsBookingModalOpen(true)}
                  className="w-full bg-red-500 hover:bg-red-600 text-white font-bold py-4 rounded-lg transition-colors shadow-lg shadow-red-100"
                >
                  Book Now
                </button>
              )}
            </div>
          </div>
        </div>

        {/* Lightbox Modal */}
        {isLightboxOpen && (
          <div className="fixed inset-0 z-[100] bg-black/95 flex items-center justify-center p-4">
            <button onClick={() => setIsLightboxOpen(false)} className="absolute top-6 right-6 text-white p-2 hover:bg-white/10 rounded-full">
              <X size={32} />
            </button>
            <img src={images[currentImg].image} className="max-w-full max-h-[90vh] object-contain" alt="Enlarged view" />
          </div>
        )}

        {/* Booking Modal */}
        {/* {isBookingModalOpen && (
          <BookingModal
            activity={activity}
            onClose={() => setIsBookingModalOpen(false)}
          />
        )} */}
      </div>
    </main >
  )
}
export default Plan
