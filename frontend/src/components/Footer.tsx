import { Link, useLocation } from 'react-router-dom';

const Footer = () => {

  const location = useLocation();
  const pathname = location.pathname;
  const isActive = (path: string) => {
    if (path === "/") return pathname === "/";
    return pathname.startsWith(path);
  };

  return (
    <footer className="border-y-1 bg-gray-100">
      <div className="container mx-auto my-6">
        {/* Link */}
        <div className="nav-link text-center md:text-right text-sm my-4 ">
          <Link to="/about/"
            className="mx-4"
            aria-current={isActive("/about/") ? "page" : undefined}>About Us |</Link>
          <Link to="/contact/"
            className="mx-4"
            aria-current={isActive("/contact/") ? "page" : undefined}>Contact |</Link>
          <Link to="/faq/"
            className="mx-4"
            aria-current={isActive("/faq/") ? "page" : undefined}>FAQ |</Link>
          <Link to="/privacy/"
            className="mx-4"
            aria-current={isActive("/privacy/") ? "page" : undefined}>Privacy |</Link>
          <Link to="/terms/"
            className="mx-4"
            aria-current={isActive("/terms/") ? "page" : undefined}>Terms & Conditions |</Link>
        </div >
        {/* Copyright */}
        < div className="text-center md:text-left ms-2" >
          <small>© Habaki, Ltd. All Rights Reserved.</small>
        </div >
      </div >
    </footer >
  );
};

export default Footer;