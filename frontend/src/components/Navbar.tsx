import { useLocation } from 'react-router-dom'; // 如果你用 React Router
// 如果還沒用 React Router，可先用 window.location.pathname

const Navbar = () => {
  // 取得目前路徑，用來判斷 active
  const pathname = window.location.pathname;

  // 輔助函式：判斷是否為 active 路徑
  const isActive = (path: string) => {
    if (path === '/') return pathname === '/';
    return pathname.startsWith(path);
  };

  // 判斷 Member 連結：已登入顯示帳戶頁，未登入顯示一般會員頁
  const memberHref = true // 假設 user.is_authenticated 為 true/false
    ? '/member/account/'   // 需替換成實際 url('member:account')
    : '/member/';

  return (
    <nav className="container mx-auto px-4">
      <div className="flex flex-col">
        {/* Logo */}
        <a
          href="/"  // 對應 {% url 'index:index' %}
          className={`border-b-2 border-black text-center text-4xl mt-2 pb-1 font-bold ${pathname === '/' ? 'text-gray-900' : 'text-gray-700'
            }`}
          aria-current={pathname === '/' ? 'page' : undefined}
        >
          Habaki
        </a>

        {/* 導覽列 */}
        <div className="py-2 border-b-2 border-black mb-2">
          <div className="flex justify-between items-center px-2 overflow-x-auto">
            <a
              href="/"  // {% url 'index:index' %}
              className={`nav-link px-3 py-2 text-lg font-medium rounded-md ${pathname === '/'
                  ? 'text-blue-700 bg-blue-50'
                  : 'text-gray-700 hover:text-blue-600 hover:bg-gray-100'
                }`}
              aria-current={pathname === '/' ? 'page' : undefined}
            >
              News
            </a>

            <a
              href="/activity/"  // {% url 'activity:activity' %}
              className={`nav-link px-3 py-2 text-lg font-medium rounded-md ${isActive('/activity/')
                  ? 'text-blue-700 bg-blue-50'
                  : 'text-gray-700 hover:text-blue-600 hover:bg-gray-100'
                }`}
              aria-current={isActive('/activity/') ? 'page' : undefined}
            >
              Activity
            </a>

            <a
              href="/collection/"  // {% url 'collection:collection' %}
              className={`nav-link px-3 py-2 text-lg font-medium rounded-md ${isActive('/collection/')
                  ? 'text-blue-700 bg-blue-50'
                  : 'text-gray-700 hover:text-blue-600 hover:bg-gray-100'
                }`}
              aria-current={isActive('/collection/') ? 'page' : undefined}
            >
              Collection
            </a>

            <a
              href="/kenshi/"  // {% url 'kenshi:kenshi' %}
              className={`nav-link px-3 py-2 text-lg font-medium rounded-md ${isActive('/kenshi/')
                  ? 'text-blue-700 bg-blue-50'
                  : 'text-gray-700 hover:text-blue-600 hover:bg-gray-100'
                }`}
              aria-current={isActive('/kenshi/') ? 'page' : undefined}
            >
              Kenshi
            </a>

            <a
              href={memberHref}  // 動態判斷登入狀態
              className={`nav-link px-3 py-2 text-lg font-medium rounded-md ${isActive('/member/')
                  ? 'text-blue-700 bg-blue-50'
                  : 'text-gray-700 hover:text-blue-600 hover:bg-gray-100'
                }`}
              aria-current={isActive('/member/') ? 'page' : undefined}
            >
              Member
            </a>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;