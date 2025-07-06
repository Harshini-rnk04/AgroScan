function selectRole(role) {
  fetch(`/set-role/${role}`)
    .then(() => {
      window.location.href = "/select-role";
    })
    .catch(error => {
      console.error("Error:", error);
    });
}
