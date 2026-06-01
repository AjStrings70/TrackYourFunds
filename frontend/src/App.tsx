import { useEffect, useState } from "react";
import { Dashboard } from "./components/Dashboard.tsx";
import { OrganizationSummary } from "./types.ts";

const defaultSummary: OrganizationSummary = {
  organizationName: "Template Manufacturing Co.",
  baseCurrency: "USD",
  totalRevenue: 0,
  totalExpenses: 0,
  taxLiability: 0,
  currencyExposure: ["USD", "XCD"],
};

function App() {
  const [summary, setSummary] = useState<OrganizationSummary>(defaultSummary);

  useEffect(() => {
    // Placeholder for API loading logic in the future.
    setSummary(defaultSummary);
  }, []);

  return (
    <div className="app-container">
      <header>
        <h1>TrackYourFunds</h1>
        <p>Business finance tracking for manufacturing and accounting teams.</p>
      </header>
      <Dashboard summary={summary} />
    </div>
  );
}

export default App;
