new gridjs.Grid({
  columns: [
    {name: "Name"},
    "Email",
    "Phone Number",
    {
        name: 'Actions',
        formatter: (cell, row) => {
          return gridjs.h('button', {
            className: 'py-2 mb-4 px-4 border rounded-md text-white bg-blue-600',
            onClick: () => alert(`Editing "${row.cells[0].data}" "${row.cells[1].data}"`)
          }, 'Edit');
        }
    },
  ],
  pagination: true,
  search: true,
  sort: true,
  data: [
    ["John", "john@example.com", "(353) 01 222 3333"],
    ["Mark", "mark@gmail.com", "(01) 22 888 4444"],
    ["Eoin", "eoin@gmail.com", "0097 22 654 00033"],
    ["Sarah", "sarahcdd@gmail.com", "+322 876 1233"],
    ["Afshin", "afshin@mail.com", "(353) 22 87 8356"]
  ]
}).render(document.getElementById("wrapper"));
