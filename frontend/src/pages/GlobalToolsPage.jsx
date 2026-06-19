import { useState, useEffect } from "react";
import Sidebar from "../components/Sidebar";
import Header from "../components/Header";
import ToolsTable from "../components/ToolsTable";
import { getTools } from "../api/toolsApi";
import { getSectors } from "../api/sectorsApi";
import { getCategories } from "../api/categoriesApi";
import { createTool } from "../api/toolsApi";

function GlobalToolsPage() {
  const [search, setSearch] = useState("");
  const [tools, setTools] = useState([]);
  const [sectors, setSectors] = useState([]);
  const [sector, setSector] = useState("");
  const [category, setCategory] = useState("");
  const [categories, setCategories] = useState([]);
  const [status, setStatus] = useState("");
  const [showModal, setShowModal] = useState(false);
  const [newTool, setNewTool] = useState({
    name: "",
    description: "",
    category: "",
    type: "",
    status: "DRAFT",
    sectors: [],
  });

  async function handleCreateTool() {
    try {
      await createTool(newTool);

      setShowModal(false);

      loadTools();
    } catch (error) {
      console.error(error);
    }
  }
  async function loadSectors() {
    try {
      const response = await getSectors();

      console.log(response.data);

      setSectors(response.data);
    } catch (error) {
      console.error(error);
    }
  }

  async function loadTools() {
    try {
      const response = await getTools(search, sector, category, status);
      console.log(response.data);
      setTools(response.data);
    } catch (error) {
      console.error("Error fetching tools:", error);
    }
  }
  async function loadCategories() {
    try {
      const response = await getCategories();
      setCategories(response.data);
    } catch (error) {
      console.error(error);
    }
  }

  useEffect(() => {
    loadTools();
  }, [search, sector, category, status]);

  useEffect(() => {
    loadSectors();
  }, []);

  useEffect(() => {
    loadCategories();
  }, []);

  return (
    <div className="layout">
      <Sidebar />

      <div className="main-content">
        <Header changeshowModal={setShowModal} />

        <div className="filters">
          <input
            className="filter-input"
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search tools..."
          />

          <select
            className="filter-select"
            value={sector}
            onChange={(e) => setSector(e.target.value)}
          >
            <option value="">All Sectors</option>
            console.log(sectors);
            {sectors.map((sector) => (
              <option key={sector.id} value={sector.name}>
                {sector.name}
              </option>
            ))}
          </select>

          <select
            className="filter-select"
            value={category}
            onChange={(e) => setCategory(e.target.value)}
          >
            <option value="">All Categories</option>

            {categories.map((category) => (
              <option key={category} value={category}>
                {category}
              </option>
            ))}
          </select>

          <select
            className="filter-select"
            value={status}
            onChange={(e) => setStatus(e.target.value)}
          >
            <option value="">All Status</option>
            <option value="DEPLOYED">Deployed</option>
            <option value="DRAFT">Draft</option>
            <option value="DISABLED">Disabled</option>
          </select>
        </div>

        <ToolsTable search={search} tools={tools} />
      </div>
      {showModal && (
        <div className="modal-overlay">
          <div className="modal">
            <h2>Create Tool</h2>

            <div className="form-group">
              <label>Tool Name</label>
              <input
                placeholder="Enter tool name"
                value={newTool.name}
                onChange={(e) =>
                  setNewTool({
                    ...newTool,
                    name: e.target.value,
                  })
                }
              />
            </div>

            <div className="form-group">
              <label>Description</label>
              <textarea
                placeholder="Enter description"
                value={newTool.description}
                onChange={(e) =>
                  setNewTool({
                    ...newTool,
                    description: e.target.value,
                  })
                }
              />
            </div>

            <div className="form-group">
              <label>Category</label>
              <input
                placeholder="Enter category"
                value={newTool.category}
                onChange={(e) =>
                  setNewTool({
                    ...newTool,
                    category: e.target.value,
                  })
                }
              />
            </div>
            <div className="form-group">
              <label>Type</label>
              <input
                placeholder="Enter type"
                value={newTool.type || ""}
                onChange={(e) =>
                  setNewTool({
                    ...newTool,
                    type: e.target.value,
                  })
                }
              />
            </div>

            <div className="form-group">
              <label>Sector</label>

              <select
                value={newTool.sectors[0] || ""}
                onChange={(e) =>
                  setNewTool({
                    ...newTool,
                    sectors: [Number(e.target.value)],
                  })
                }
              >
                <option value="">Select Sector</option>

                {sectors.map((sector) => (
                  <option key={sector.id} value={sector.id}>
                    {sector.name}
                  </option>
                ))}
              </select>
            </div>

            <div className="modal-actions">
              <button
                className="cancel-btn"
                onClick={() => setShowModal(false)}
              >
                Cancel
              </button>

              <button className="save-btn" onClick={handleCreateTool}>
                Save Tool
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default GlobalToolsPage;
