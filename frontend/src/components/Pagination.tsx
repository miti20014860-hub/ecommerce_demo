interface PaginationProps {
  current: number;
  totalCount: number;
  pageSize: number;
  onPageChange: (page: number) => void;
}

export const Pagination = ({ current, totalCount, pageSize, onPageChange }: PaginationProps) => {
  const totalPages = Math.ceil(totalCount / pageSize);
  if (totalPages <= 1) return null;

  return (
    <div className="flex justify-center items-center mt-5 mb-1">
      <button
        disabled={current === 1}
        onClick={() => onPageChange(current - 1)}
        className="p-1 rounded-s border border-gray-300 text-gray-600 hover:bg-slate-50 hover:text-slate-700 disabled:opacity-30 disabled:cursor-not-allowed"
      >
        Prev
      </button>

      {[...Array(totalPages)].map((_, i) => {
        const p = i + 1;
        return (
          <button
            key={p}
            onClick={() => onPageChange(p)}
            className={`p-1 w-8 border border-gray-300 text-gray-600 transition-colors ${current === p ? 'border-slate-300 bg-slate-300 text-white' : 'hover:bg-slate-50 hover:text-slate-700'
              }`}
          >
            {p}
          </button>
        );
      })}

      <button
        disabled={current === totalPages}
        onClick={() => onPageChange(current + 1)}
        className="p-1 rounded-e border border-gray-300 text-gray-600 hover:bg-slate-50 hover:text-slate-700 disabled:opacity-30 disabled:cursor-not-allowed"
      >
        Next
      </button>
    </div>
  );
};

export default Pagination