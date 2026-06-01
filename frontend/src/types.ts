export interface OrganizationSummary {
  organizationName: string;
  baseCurrency: string;
  totalRevenue: number;
  totalExpenses: number;
  taxLiability: number;
  currencyExposure: string[];
}
