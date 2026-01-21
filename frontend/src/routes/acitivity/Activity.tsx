import { useState } from 'react';

export default function Activity() {
  const [priceRange, setPriceRange] = useState([0, 1000]);
  const [selectedCategories, setSelectedCategories] = useState<string[]>([]);
  const [selectedSort, setSelectedSort] = useState('newest');
  const [isOpen, setIsOpen] = useState(false);

  const toggleCategory = (category: string) => {
    setSelectedCategories(prev =>
      prev.includes(category)
        ? prev.filter(c => c !== category)
        : [...prev, category]
    );
  };

  const resetFilters = () => {
    setPriceRange([0, 1000]);
    setSelectedCategories([]);
    setSelectedSort('newest');
  };

  return (
    <main className='container mx-auto lg:px-8 xl:px-16 2xl:px-24 font-serif'>
      {/* Open button */}
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
      <aside
        className={`fixed inset-y-0 left-0 z-2 w-70 bg-white shadow-xl lg:relative lg:translate-x-0 ${isOpen ? 'translate-x-0' : '-translate-x-full'}`}
      >
        <div className="h-full flex flex-col">
          {/* 標題 + 關閉按鈕 */}
          <div className="p-6 border-b flex items-center justify-between lg:hidden">
            <h2 className="text-xl font-bold">篩選條件</h2>
            <button onClick={() => setIsOpen(false)} className="text-gray-500 hover:text-gray-700">
              <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>

          {/* 篩選內容 */}
          <div className="flex-1 overflow-y-auto p-6 space-y-8">
            {/* 類別 */}
            <div>
              <h3 className="font-semibold mb-3">類別</h3>
              <div className="space-y-2">
                {['全部', '新聞', '公告', '活動', '收藏'].map(cat => (
                  <label key={cat} className="flex items-center">
                    <input
                      type="checkbox"
                      checked={selectedCategories.includes(cat)}
                      onChange={() => toggleCategory(cat)}
                      className="rounded border-gray-300 text-blue-600 focus:ring-blue-500"
                    />
                    <span className="ml-2">{cat}</span>
                  </label>
                ))}
              </div>
            </div>

            {/* 價格範圍（範例） */}
            <div>
              <h3 className="font-semibold mb-3">價格範圍</h3>
              <input
                type="range"
                min="0"
                max="1000"
                value={priceRange[1]}
                onChange={e => setPriceRange([priceRange[0], Number(e.target.value)])}
                className="w-full"
              />
              <div className="flex justify-between text-sm text-gray-600 mt-2">
                <span>$0</span>
                <span>${priceRange[1]}</span>
              </div>
            </div>

            {/* 排序 */}
            <div>
              <h3 className="font-semibold mb-3">排序</h3>
              <select
                value={selectedSort}
                onChange={e => setSelectedSort(e.target.value)}
                className="w-full border rounded-lg p-2 focus:ring-2 focus:ring-blue-500"
              >
                <option value="newest">最新</option>
                <option value="oldest">最舊</option>
                <option value="popular">熱門</option>
              </select>
            </div>
          </div>

          {/* 按鈕區 */}
          <div className="p-6 border-t">
            <button
              onClick={resetFilters}
              className="w-full py-3 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300 transition"
            >
              重置篩選
            </button>
            <button
              onClick={() => {/* 這裡送出篩選條件 */ }}
              className="w-full py-3 mt-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
            >
              套用篩選
            </button>
          </div>
        </div>
      </aside>

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