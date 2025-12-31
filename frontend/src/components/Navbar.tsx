import { Link, useLocation } from 'react-router-dom';

const Navbar = () => {

  const location = useLocation();
  const pathname = location.pathname;
  const isActive = (path: string) => {
    if (path === "/") return pathname === "/";
    return pathname.startsWith(path);
  };

  const isAuthenticated = window.currentUser?.isAuthenticated || false;
  const memberHref = isAuthenticated ? "/member/account/" : "/member/";

  return (
    <nav className="container mx-auto font-serif">
      {/* Logo */}
      <div className="nav-link flex justify-center">
        <Link to="/" className="text-3xl mt-3 mb-2">Habaki</Link>
      </div>
      {/* Link */}
      <div className="border-y-1 border-gray-500 py-1 mb-2">
        <div className="nav-link flex justify-between overflow-x-auto px-3 text-lg">
          <Link to="/"
            className={`px-3 py-1 ${pathname === "/" ? "border-b-2" : "hover:border-b-2"}`}
            aria-current={pathname === "/" ? "page" : undefined}>News</Link>
          <Link to="/activity/"
            className={`px-3 py-1 ${isActive("/activity/") ? "border-b-2" : "hover:border-b-2"}`}
            aria-current={isActive("/activity/") ? "page" : undefined}>Activity</Link>
          <Link to="/collection/"
            className={`px-3 py-1 ${isActive("/collection/") ? "border-b-2" : "hover:border-b-2"}`}
            aria-current={isActive("/collection/") ? "page" : undefined}>Collection</Link>
          <Link to="/kenshi/"
            className={`px-3 py-1 ${isActive("/kenshi/") ? "border-b-2" : "hover:border-b-2"}`}
            aria-current={isActive("/kenshi/") ? "page" : undefined}>Kenshi</Link>
          <Link to={memberHref}
            className={`px-3 py-1 ${isActive("/member/") ? "border-b-2" : "hover:border-b-2"}`}
            aria-current={isActive("/member/") ? "page" : undefined}>Member</Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
