function ToolsTable({ search, tools }) {
  const statusClasses = {
    DEPLOYED: "status-deployed",
    DRAFT: "status-draft",
    DISABLED: "status-disabled",
  };

  return (
    <table className="tools-table">
      <thead>
        <tr>
          <th>Name</th>
          <th>Sector</th>
          <th>Category</th>
          <th>Type</th>
          <th>Status</th>
        </tr>
      </thead>

      <tbody>
        {tools?.map((tool) => (
          <tr key={tool.id}>
            <td>
              <div className="tool-name">{tool.name}</div>

              <div className="tool-description">{tool.description}</div>
            </td>
            <td>
              <span className="sector-badge">{tool.sector_names?.[0]}</span>
            </td>
            <td>{tool.category}</td>
            <td>{tool.type}</td>
            <td>
              <span className={statusClasses[tool.status]}>{tool.status}</span>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default ToolsTable;
