const cpuValue = document.getElementById('cpu-value');
const memoryValue = document.getElementById('memory-value');
const diskValue = document.getElementById('disk-value');
const serverStatusValue = document.getElementById('status-value');
const serverStatusDetail = document.getElementById('status-detail');
const alertsValue = document.getElementById('alert-value');
const alertsDetail = document.getElementById('alert-detail');

function animateValue(element, start, end, duration) {

    let startTimestamp = null;

    function step(timestamp) {

        if (!startTimestamp)
            startTimestamp = timestamp;

        const progress = Math.min(
            (timestamp - startTimestamp) / duration,
            1
        );

        const value =
            progress * (end - start) + start;

        element.innerText =
            `${value.toFixed(2)}%`;

        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    }

    window.requestAnimationFrame(step);
}

async function loadMetrics() {

    try {

        const response = await fetch(
            "https://8c19a36e6i.execute-api.ap-south-1.amazonaws.com/prod/metrics"
        );

        if (!response.ok) {
            throw new Error("API request failed");
        }

        const data =
            await response.json();

        console.log(
            "Metrics:",
            data
        );

        const cpu =
            data.cpu_utilization?.average ?? 0;

        const memory =
            data.memory_utilization?.average ?? 0;

        const disk =
            data.disk_utilization?.average ?? 0;

        // Animated numbers
        animateValue(
            cpuValue,
            parseFloat(cpuValue.innerText) || 0,
            cpu,
            1000
        );

        animateValue(
            memoryValue,
            parseFloat(memoryValue.innerText) || 0,
            memory,
            1000
        );

        animateValue(
            diskValue,
            parseFloat(diskValue.innerText) || 0,
            disk,
            1000
        );

        // Status + Alerts
        if (cpu < 80) {

            serverStatusValue.innerText =
                'Online 🟢';

            serverStatusDetail.innerText =
                'All systems are operating normally.';

            alertsValue.innerText =
                'No Alerts';

            alertsDetail.innerText =
                'No active alerts detected.';

        } else {

            serverStatusValue.innerText =
                'Warning 🟡';

            serverStatusDetail.innerText =
                'High CPU usage detected.';

            alertsValue.innerText =
                'High CPU';

            alertsDetail.innerText =
                'CPU usage exceeded threshold.';
        }

    } catch (error) {

        console.error(
            "Fetch Error:",
            error
        );

        cpuValue.innerText =
            "Error";

        memoryValue.innerText =
            "Error";

        diskValue.innerText =
            "Error";

        serverStatusValue.innerText =
            "Unavailable";

        alertsValue.innerText =
            "Connection Error";
    }
}

loadMetrics();
setInterval(loadMetrics, 10000);