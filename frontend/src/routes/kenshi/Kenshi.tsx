import { useQuery } from '@tanstack/react-query';
import { fetchKenshi } from '@/lib/fetcher';

export const Kenshi = () => {
  const { data: kenshi, isLoading, isError, error } = useQuery({
    queryKey: ['kenshi'],
    queryFn: () => fetchKenshi(),
  });

  if (isLoading) { return <div className='text-center py-20'>Loading...</div>; }
  if (isError || !kenshi) { return <div className='text-center py-20'>Loading failed: {error?.message}</div>; }

  return (
    <main className='bg-white'>
      {kenshi.map((kenjyutsuka) => (
        <section className='aspect-video overflow-hidden'>
          <video loop muted autoPlay playsInline
            key={kenjyutsuka.id}
            src={kenjyutsuka.video}
            className='w-full h-full object-cover'
          />
        </section>
      ))}

      {kenshi.map((kenjyutsuka) => (
        <article className='container mx-auto 2xl:px-24 p-2'>
          <h2 className='bg-gray-50 border-b-5 text-3xl sm:text-[33px] lg:text-4xl font-medium text-center p-1 mb-3'>{kenjyutsuka.title}</h2>
          <div className='grid lg:grid-cols-2'>
            <div className='lg:col-span-1'>
              <img
                key={kenjyutsuka.id}
                src={kenjyutsuka.image}
                alt={kenjyutsuka.title || 'Poster'}
                className='w-full'
              />
            </div>
            <div className='lg:col-span-1 bg-gray-50 px-5'>
              <p className='whitespace-pre-wrap mt-3'>{kenjyutsuka.content}</p>
            </div>
          </div>
        </article>
      ))}
    </main>
  )
}

export default Kenshi
