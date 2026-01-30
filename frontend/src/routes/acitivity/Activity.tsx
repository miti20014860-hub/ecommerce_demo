import { useState } from 'react';
import SearchInput from '@/components/SearchInput';


export default function Activity() {
  const [isOpen, setIsOpen] = useState(false);
  const [search, setSearch] = useState('');

  return (
    <main className='container mx-auto lg:px-8 xl:px-16 2xl:px-24 font-serif'>
      {/* Open */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="lg:hidden fixed bottom-4 right-4 bg-gray-400 text-white px-6 py-3 rounded-full shadow-md flex items-center gap-2"
      >
        <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" />
        </svg>
        Filter
      </button>
      {/* Sidebar */}
      <div className='grid lg:grid-cols-3'>
        <aside
          className={`fixed inset-y-0 left-0 z-2 bg-white shadow-xl lg:col-span-1 lg:relative lg:translate-x-0 ${isOpen ? 'translate-x-0' : '-translate-x-full'}`}
        >
          {/* Filter */}
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
            <div className="mb-6 max-w-md">
              <SearchInput
                onSearch={setSearch}
                placeholder="Search..."
              />
            </div>
          </div>
        </aside>
        {/* List */}
        <div className='lg:col-span-2 bg-yellow-100'>
          <p>{search}</p>
        </div>
      </div>
      {/* Mask */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black/50 lg:hidden z-1"
          onClick={() => setIsOpen(false)}
        />
      )}
    </main>
  );
}