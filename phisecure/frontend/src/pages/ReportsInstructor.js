import { Chart } from "react-google-charts";

export const dataInstructor = [
    ["Course", "54631", "", ""],
    ["", "", "Number of Attacks with Reactions", "Number of Accounts Phished"],
    ["Red Flags Missed", "75%","150","200"],
    ["Links Clicked", "25%","50",""],
    ["Compromising Replies", "60%","120",""],
    ["Successful Attacks", "50%","100",""],
    ["Most Successful Platfrom", "Email","",""],
    ["Least Successful Platform", "Zoom","",""],
    ["Most Successful Template", "professor2(email)","",""],
    ["Least Successful Template", "momCall(Zoom)","",""]
  ];
  
  export const optionsInstructor = {
    title: "Instructor Report",
    curveType: "function",
    legend: { position: "bottom" },
    pageSize: 10,
    allowHtml: true,
  };

  export function ReportsInstructor() {
    return (
      <div id="instructor_report">
          <meta charSet="UTF-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0" />
          <title>Phisecure - Contact</title>
          <link rel="stylesheet" href="styles.css" />
          {/* Main Content */}
          <main>
          <section className="report-section">
              <h2>Instructor Report</h2>
              <Chart
              chartType="Table"
              width="100%"
              height="400px"
              data={dataInstructor}
              options={optionsInstructor}
              />
          </section>
          </main>
          {/* Footer */}
          <footer>
          <p>© 2024 Phisecure. All rights reserved.</p>
          </footer>
      </div>
    )
  }