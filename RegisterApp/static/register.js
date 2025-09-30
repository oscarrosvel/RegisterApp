// Al comienzo del archivo:
const {
  allowed_tabs,
  rol,
  session_user,
  razones,
  roles,
  restaurantes,
  tables_cfg
} = window.APP_DATA || {};

// Y luego reutilizas estas constantes en todo el script:
const ALLOWED_TABS = new Set(allowed_tabs || []);
const USER_ROLE = rol || '';
const currentUser = session_user || '';
const _razones = razones || [];
const _roles = roles || [];
const _restaurantes = restaurantes || [];
const TABLES_CFG = tables_cfg || {};
