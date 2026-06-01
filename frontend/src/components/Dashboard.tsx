import { OrganizationSummary } from "../types";

interface DashboardProps {
  summary: OrganizationSummary;
}

export function Dashboard({ summary }: DashboardProps) {
  return (
    <main>
      <section className="summary-card">
        <h2>{summary.organizationName}</h2>
        <p>Base currency: {summary.baseCurrency}</p>
      </section>

      <section className="metrics-grid">
        <article>
          <h3>Total Revenue</h3>
          <p>{summary.baseCurrency} {summary.totalRevenue.toLocaleString()}</p>
        </article>
        <article>
          <h3>Total Expenses</h3>
          <p>{summary.baseCurrency} {summary.totalExpenses.toLocaleString()}</p>
        </article>
        <article>
          <h3>Tax Liability</h3>
          <p>{summary.baseCurrency} {summary.taxLiability.toLocaleString()}</p>
        </article>
        <article>
          <h3>Supported Currencies</h3>
          <p>{summary.currencyExposure.join(", ")}</p>
        </article>
      </section>
    </main>
  );
}
