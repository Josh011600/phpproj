<!DOCTYPE html>
<html>
<head>
    <title>JS + MySQL Data</title>
</head>
<body>
    <h1>Data from MySQL (via Flask)</h1>
    <table border="1" id="data-table">
        <thead>
            <tr id="headers"></tr>
        </thead>
        <tbody id="table-body"></tbody>
    </table>

    <script>
        fetch('/api/data')
            .then(response => response.json())
            .then(data => {
                const headers = document.getElementById('headers');
                const body = document.getElementById('table-body');

                if (data.length > 0) {
                    // Create table headers
                    Object.keys(data[0]).forEach(key => {
                        const th = document.createElement('th');
                        th.textContent = key;
                        headers.appendChild(th);
                    });

                    // Create table rows
                    data.forEach(row => {
                        const tr = document.createElement('tr');
                        Object.values(row).forEach(value => {
                            const td = document.createElement('td');
                            td.textContent = value;
                            tr.appendChild(td);
                        });
                        body.appendChild(tr);
                    });
                }
            })
            .catch(error => console.error('Error fetching data:', error));
    </script>
</body>
</html>
