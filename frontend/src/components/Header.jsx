function Header({changeshowModal}) {
  return (
    <div className="header">
      <div className="page-header">
        <div>
          <h1>Global Tools Management</h1>
          <p className="page-subtitle">
            Manage all global tools across the platform
          </p>
        </div>

        <button className="create-btn" onClick={() => changeshowModal(true)}>
          + Create Tool
        </button>
      </div>
    </div>
  );
}

export default Header;