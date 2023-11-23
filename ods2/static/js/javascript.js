const sidebar = document.querySelector('.sidebar');

const toggleSidebar = () => {
  sidebar.classList.toggle('hidden');
};

const toggleSidebarButton = document.querySelector('#toggleSidebarButton');

toggleSidebarButton.addEventListener('click', toggleSidebar);