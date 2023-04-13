// Pelanggan pie chart
var ctx = document.getElementById("pelanggan").getContext("2d");
var myPieChart = new Chart(ctx, {
  type: "pie",
  data: {
    labels: ["store_a", "store_b", "store_c"],
    datasets: [
      {
        label: "My First Dataset",
        data: [50, 25, 25],
        backgroundColor: ["orange", "green", "blue"],
        borderColor: "white",
        borderWidth: 1,
      },
    ],
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: "top",
      },
    },
  },
});

// Pesanan pie chart
var ctx = document.getElementById("pesanan").getContext("2d");
var myPieChart = new Chart(ctx, {
  type: "pie",
  data: {
    labels: ["Belum Diproses", "Diproses"],
    datasets: [
      {
        label: "My First Dataset",
        data: [50, 50],
        backgroundColor: ["orange", "green"],
        borderColor: "white",
        borderWidth: 1,
      },
    ],
  },
  options: {
    responsive: true,
    plugins: {
      legend: {
        position: "top",
      },
    },
  },
});

// Scrolled