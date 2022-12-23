
window.addEventListener("DOMContentLoaded", () => {
  function searchHandler(e) {
    e.preventDefault();
    let searchField = document.getElementById("searchField");
    let keyword = searchField.value;
    searchField.value = ""
  }

  // const searchForm = document.getElementById("searchForm");
  // searchForm.addEventListener("submit", searchHandler);
});
