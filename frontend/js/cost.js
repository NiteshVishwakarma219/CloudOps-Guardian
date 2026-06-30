async function loadCost() {
    const data = await fetchData("/cost");

    // Top Summary Cards
    document.getElementById("costCards").innerHTML = `
        <div class="card">
            <h3>Total Monthly Cost</h3>
            <p>$${data.total_cost}</p>
        </div>

        <div class="card">
            <h3>Estimated Savings</h3>
            <p>$${data.savings}</p>
        </div>

        <div class="card">
            <h3>Idle EC2</h3>
            <p>${data.idle_ec2}</p>
        </div>

        <div class="card">
            <h3>Unused EBS</h3>
            <p>${data.unused_ebs}</p>
        </div>

        <div class="card">
            <h3>Orphaned Snapshots</h3>
            <p>${data.orphan_snapshots}</p>
        </div>

        <div class="card">
            <h3>Idle Elastic IPs</h3>
            <p>${data.idle_eip}</p>
        </div>
    `;

    // Idle Resources List
    let idleHTML = "";

    data.idle_resources.forEach(item => {
        idleHTML += `
            <div class="card" style="border-left: 5px solid orange;">
                <h4>${item.type}</h4>
                <p>${item.name}</p>
                <small>Potential Savings: $${item.savings}</small>
            </div>
        `;
    });

    document.getElementById("idleResources").innerHTML = idleHTML;

    // Chart (VERY IMPORTANT FOR INTERVIEWS)
    const ctx = document.getElementById("savingsChart");

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: ["EC2", "EBS", "Snapshots", "Elastic IPs"],
            datasets: [{
                label: "Savings ($)",
                data: [
                    data.chart.ec2,
                    data.chart.ebs,
                    data.chart.snapshots,
                    data.chart.eip
                ]
            }]
        }
    });
}

loadCost();