// import { useLocation } from 'react-router-dom'; // React Router

const Navbar = () => {
  const pathname = window.location.pathname;

  const isActive = (path: string) => {
    if (path === '/') return pathname === '/';
    return pathname.startsWith(path);
  };

  const isAuthenticated = window.currentUser?.isAuthenticated || false;

  const memberHref = isAuthenticated
    ? '/member/account/'
    : '/member/';

  return (
    <nav className="container mx-auto font-medium">
      <div className="nav-link flex justify-center">
        {/* Logo */}
        <a href="/" className="text-3xl mt-3 mb-2">
          Habaki
        </a>
      </div>
      {/* Navbar */}
      <div className="border-y-2 border-gray-500 py-1 mb-2">
        <div className="nav-link flex justify-between overflow-x-auto px-3 text-xl">
          <a href="/"  // {% url 'index:index' %}
            className={`px-3 py-2 ${pathname === '/'
              ? 'border-b-2'
              : 'hover:border-b-2'
              }`}
            aria-current={pathname === '/' ? 'page' : undefined}
          >
            News
          </a>

          <a href="/activity/"  // {% url 'activity:activity' %}
            className={`px-3 py-2 ${isActive('/activity/')
              ? 'border-b-2'
              : 'hover:border-b-2'
              }`}
            aria-current={isActive('/activity/') ? 'page' : undefined}
          >
            Activity
          </a>

          <a href="/collection/"  // {% url 'collection:collection' %}
            className={`px-3 py-2 ${isActive('/collection/')
              ? 'border-b-2'
              : 'hover:border-b-2'
              }`}
            aria-current={isActive('/collection/') ? 'page' : undefined}
          >
            Collection
          </a>

          <a href="/kenshi/"  // {% url 'kenshi:kenshi' %}
            className={`px-3 py-2 ${isActive('/kenshi/')
              ? 'border-b-2'
              : 'hover:border-b-2'
              }`}
            aria-current={isActive('/kenshi/') ? 'page' : undefined}
          >
            Kenshi
          </a>

          <a href={memberHref}  // Dynamically determine login status
            className={`px-3 py-2 ${isActive('/member/')
              ? 'border-b-2'
              : 'hover:border-b-2'
              }`}
            aria-current={isActive('/member/') ? 'page' : undefined}
          >
            Member
          </a>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;