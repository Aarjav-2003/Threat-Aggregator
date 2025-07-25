document.getElementById("csvFileInput").addEventListener("change", function (e) {
  const file = e.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = function (event) {
    const lines = event.target.result.split("\n").slice(1); // skip header
    const tableBody = document.querySelector("#iocTable tbody");
    tableBody.innerHTML = "";

    for (const line of lines) {
      if (line.trim() === "") continue;
      const [source, ioc_type, value, timestamp] = line.split(",");
      const row = document.createElement("tr");

      [source, ioc_type, value, timestamp].forEach((cellText) => {
        const cell = document.createElement("td");
        cell.textContent = cellText;
        row.appendChild(cell);
      });

      tableBody.appendChild(row);
    }
  };
  reader.readAsText(file);
});
