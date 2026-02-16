import { useParams } from 'react-router-dom';
import { useQuery } from '@tanstack/react-query';
import { useState } from 'react';
import { fetchCollectionById } from '@/lib/fetcher';
import OrderModal from '@/components/CollectionOrder';

export const CollectionDetail = () => {
  const { id } = useParams<{ id: string }>();
  const { data: collection, isLoading, isError, error } = useQuery({
    queryKey: ['collection', id],
    queryFn: () => fetchCollectionById(Number(id)),
    enabled: !!id,
  });

  const [isOrderModalOpen, setIsOrderModalOpen] = useState(false);

  const val = (value: string | number | undefined | null) => value || '－';

  if (isLoading) { return <div className='text-center py-20'>Loading...</div>; }
  if (isError || !collection) { return <div className='text-center py-20'>Loading failed: {error?.message}</div>; }

  return (
    <main className='container mx-auto lg:px-16 xl:px-32 2xl:px-64 px-2'>
      <div className='border border-gray-800'>

        {/* Name Header */}
        <div className='bg-gray-500 p-2 text-center'>
          <h2 className='text-2xl sm:text-[26px] tracking-wider mt-1'>{val(collection.name_jp)}</h2>
          <h2 className='text-xl sm:text-2xl font-medium'>{val(collection.name_en)}</h2>
        </div>

        {/* Provider + Signature + Type */}
        <div className='grid grid-cols-3 border-b border-gray-300'>
          <div className='col-span-2 bg-gray-50/50'>
            <div className='grid grid-cols-3 md:grid-cols-5 p-2 items-center border-b border-white'>
              <span className='col-span-1'>Provider</span>
              <span className='col-span-2 md:col-span-4'>{val(collection.provider)}</span>
            </div>
            <div className='grid grid-cols-3 md:grid-cols-5 p-2 items-center'>
              <span className='col-span-1'>Signature</span>
              <span className='col-span-2 md:col-span-4'>{val(collection.signature)}</span>
            </div>
          </div>
          <div className='col-span-1 bg-gray-300/50 flex items-center justify-center'>
            <h3 className='text-[26px] px-4 pb-1'>
              {val(collection.type_display)}
            </h3>
          </div>
        </div>

        {/* Size Specifications Grid */}
        <div className='grid grid-cols-2 border-b border-gray-300 items-center'>
          {/* Labels Left */}
          <div className='col-span-1 bg-gray-300/50'>
            <div className='grid grid-cols-10 md:grid-cols-2 items-center border-b border-white p-2'>
              <p className='col-span-6 md:col-span-1'>Blade Length</p>
              <p className='col-span-4 md:col-span-1 md:ms-2'>{val(collection.blade_length)} cm</p>
            </div>
            <div className='grid grid-cols-10 md:grid-cols-2 items-center border-b border-white p-2'>
              <p className='col-span-6 md:col-span-1'>Curvature</p>
              <p className='col-span-4 md:col-span-1 md:ms-2'>{val(collection.curvature)} cm</p>
            </div>
            <div className='grid grid-cols-10 md:grid-cols-2 items-center border-b border-white p-2'>
              <p className='col-span-6 md:col-span-1'>Sword Weight</p>
              <p className='col-span-4 md:col-span-1 md:ms-2'>{val(collection.sword_weight)} g</p>
            </div>
            <div className='grid grid-cols-10 md:grid-cols-2 items-center p-2'>
              <p className='col-span-6 md:col-span-1'>Period</p>
              <p className='col-span-4 md:col-span-1 md:ms-2'>{val(collection.period)}</p>
            </div>
          </div>

          {/* Labels Right */}
          <div className='col-span-1 bg-gray-50/50'>
            <div className='grid grid-cols-10 md:grid-cols-2 items-center border-b border-white p-2'>
              <p className='col-span-6 md:col-span-1'>Motohaba</p>
              <p className='col-span-4 md:col-span-1 md:ms-2'>{val(collection.motohaba)} cm</p>
            </div>
            <div className='grid grid-cols-10 md:grid-cols-2 items-center border-b border-white p-2'>
              <p className='col-span-6 md:col-span-1'>Sakihaba</p>
              <p className='col-span-4 md:col-span-1 md:ms-2'>{val(collection.sakihaba)} cm</p>
            </div>
            <div className='grid grid-cols-10 md:grid-cols-2 items-center border-b border-white p-2'>
              <p className='col-span-6 md:col-span-1'>Motogasane</p>
              <p className='col-span-4 md:col-span-1 md:ms-2'>{val(collection.motogasane)} cm</p>
            </div>
            <div className='grid grid-cols-10 md:grid-cols-2 items-center p-2'>
              <p className='col-span-6 md:col-span-1'>Sakigasane</p>
              <p className='col-span-4 md:col-span-1 md:ms-2'>{val(collection.sakigasane)} cm</p>
            </div>
          </div>
        </div>

        {/* Koshirae + Registration + Certificate */}
        <div className='border-b border-gray-300 bg-gray-300/50 '>
          <div className='grid grid-cols-7 md:grid-cols-4 border-b border-white items-center'>
            <p className='col-span-2 md:col-span-1 p-2'>Koshirae</p>
            <p className='col-span-5 md:col-span-3 bg-white p-2'>{val(collection.koshirae)}</p>
          </div>
          <div className='grid grid-cols-7 md:grid-cols-4 border-b border-white items-center'>
            <p className='col-span-2 md:col-span-1 p-2'>Registration</p>
            <p className='col-span-5 md:col-span-3 bg-white p-2'>{val(collection.registration)}</p>
          </div>
          <div className='grid grid-cols-7 md:grid-cols-4 items-center'>
            <p className='col-span-2 md:col-span-1 p-2'>Certificate</p>
            <p className='col-span-5 md:col-span-3 bg-white p-2'>{val(collection.certificate)}</p>
          </div>
        </div>

        {/* Remarks + Price */}
        <div className='grid md:grid-cols-3 border-b border-gray-300'>
          <div className='md:col-span-2 bg-gray-50/50 p-2'>
            <span className='block mb-1 uppercase'>Remarks</span>
            <p className='whitespace-pre-wrap leading-relaxed'>
              {val(collection.remarks)}
            </p>
          </div>
          <div className='md:col-span-1 bg-gray-300/50 flex flex-col items-center justify-center p-2'>
            <div className='flex items-baseline gap-1'>
              <span className='text-[27px] font-medium'>{Number(collection.price).toLocaleString()}</span>
              <span className='text-xl font-medium'>{collection.currency}</span>
            </div>
            <span className='font-medium'>(Tax excluded)</span>
          </div>
        </div>

        {/* Order link */}
        <div className='p-2 text-center'>
          <button
            onClick={() => setIsOrderModalOpen(true)}
            className='text-yellow-900 font-bold hover:text-yellow-700 hover:underline cursor-pointer'
          >
            [Open Order Form]
          </button>
        </div>
      </div>

      {/* Images Section */}
      <div className=''>
        {collection.images && collection.images.length > 0 ? (
          collection.images.map((img, index) => (
            <div key={index} className='w-full'>
              <img
                src={img.image}
                alt={img.caption || `Collection Image ${index + 1}`}
                className='w-full h-auto object-cover'
              />
            </div>
          ))
        ) : (
          <div className='p-10 text-center border-2 border-dashed border-slate-200 text-slate-400'>
            No Images Available
          </div>
        )}

        <div className='text-center mt-3'>
          <button
            onClick={() => window.scrollTo({ top: 0, behavior: 'smooth' })}
            className='font-medium hover:underline'
          >
            [Back to Top]
          </button>
        </div>
      </div>

      {/* Order */}
      {isOrderModalOpen && (
        <OrderModal
          collection={collection}
          onClose={() => setIsOrderModalOpen(false)}
        />
      )}
    </main >
  )
}
export default CollectionDetail
