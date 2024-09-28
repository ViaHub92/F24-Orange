import { Chart } from "react-google-charts";

export const dataStudentAttack = [
  ["Name", "Doe, John", "Class ID", "02451121"],
  ["Successful Attacks", "3", "UID", "233023"],
  ["Best Platform", "Facebook","",""],
  ["Worst Platform", "Discord","",""],
  ["Overall Grade", "64%","",""],
];

export const optionsStudentAttack = {
  title: "Student Report",
  curveType: "function",
  legend: { position: "bottom" },
  pageSize: 5,
};

export const dataStudentDefend = [
    ["Name", "Doe, John", "Class ID", "02451121"],
    ["Links Clicked", "3", "UID", "233023"],
    ["Red Flags Missed", "3","",""],
    ["Number of Emails Reported", "4","",""],
    ["Overall Grade", "72%","",""],
  ];
  
  export const optionsStudentDefend = {
    title: "Student Report",
    curveType: "function",
    legend: { position: "bottom" },
    pageSize: 5,
  };

export function ReportsStudents() {
  return (
    <div>
        <meta charSet="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Phisecure - Contact</title>
        <link rel="stylesheet" href="styles.css" />
        {/* Main Content */}
        <main>
        <section className="section">
            <h2>Attacker Report</h2>
            <Chart
            chartType="Table"
            width="100%"
            height="400px"
            data={dataStudentAttack}
            options={optionsStudentAttack}
            />
        </section>
        <section className="section">
            <h2>Defender Report</h2>
            <Chart
            chartType="Table"
            width="100%"
            height="400px"
            data={dataStudentDefend}
            options={optionsStudentDefend}
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
