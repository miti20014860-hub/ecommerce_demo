import { useState, useEffect } from 'react';
import { useDebounce } from 'use-debounce';
import { Search } from 'lucide-react';
import type { ChangeEvent } from 'react';

interface SearchInputProps {
  onSearch: (value: string) => void;
  placeholder?: string;
  className?: string;
}

export default function SearchInput({
  onSearch,
  placeholder = "Search...",
  className = "",
}: SearchInputProps) {
  const [value, setValue] = useState('');
  const debouncedValue = useDebounce(value, 1000)[0];

  useEffect(() => {
    if (debouncedValue !== undefined) {
      onSearch(debouncedValue.trim());
    }
  }, [debouncedValue, onSearch]);

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const newValue = e.target.value;
    setValue(newValue);
  };

  return (
    <div className={`relative ${className}`}>
      <div className="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
        <Search className="w-5 h-5 text-gray-400" />
      </div>

      <input
        type="search"
        value={value}
        onChange={handleChange}
        placeholder={placeholder}
        className={`
          w-full pl-10 pr-4 py-2.5
          bg-white border border-gray-300
          text-gray-900 text-sm rounded-lg
          focus:ring-2 focus:ring-blue-500 focus:border-blue-500
          outline-none transition-all
          placeholder:text-gray-400
        `}
        autoComplete="off"
        spellCheck={false}
      />
    </div>
  );
}