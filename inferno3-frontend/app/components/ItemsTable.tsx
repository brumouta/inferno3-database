'use client'
import {Container} from "@mui/material";
import {DataGrid, GridColDef, GridToolbar, ptBR} from "@mui/x-data-grid";
import styles from './styles.module.css'
import {Item} from "@/types/item";

const formatArray = (params: any) => {
  return String(params.value).replaceAll(',', '\n');
};

const formatEffects = (params: any) => {
  let effects = '';
  Object.entries(params.value).forEach(([key, value], index) => {
    effects += `${key}: ${value}\n`;
  });
  return effects;
};

const columns: GridColDef[] = [
  {field: 'name', headerName: 'Nome', width: 300},
  {field: 'type', headerName: 'Tipo', width: 100},
  {field: 'level', headerName: 'Level', width: 80},
  {field: 'remort', headerName: 'Remort', width: 100},
  {field: 'value', headerName: 'Valor', width: 100},
  {field: 'weight', headerName: 'Peso', width: 80},
  {field: 'dice', headerName: 'Dado de Dano', width: 80},
  {field: 'damage', headerName: 'Dano médio', width: 80},
  {field: 'armor', headerName: 'Armadura', width: 120},
  {field: 'slot', headerName: 'Local', width: 120},
  {
    field: 'abilities',
    headerName: 'Habilidades',
    width: 130,
    valueFormatter: formatArray
  },
  {
    field: 'properties',
    headerName: 'Propriedades',
    width: 150,
    valueFormatter: formatArray
  },
  {
    field: 'effects',
    headerName: 'Afetamentos',
    width: 130,
    valueFormatter: formatEffects
  },
  {field: 'prevents', headerName: 'Prevenir', width: 120},
  {field: 'capacity', headerName: 'Capacidade', width: 100},
  {field: 'wand', headerName: 'Varinha', width: 100},
  {field: 'mob', headerName: 'Mob', width: 100},
  {field: 'seller', headerName: 'Vendedor', width: 100},
  {field: 'price', headerName: 'Preço', width: 100},
  {field: 'room', headerName: 'Sala', width: 100},
  {field: 'area', headerName: 'Área', width: 100},
];


interface Props {
  items: Item[];
  quickFilter?: string;
}

const ItemsTable = ({items, quickFilter}: Props) => {
  return (
      <Container>
        <DataGrid
            initialState={{
              filter: {
                filterModel: {
                  items: [],
                  quickFilterValues: [quickFilter],
                },
              },
            }}
            experimentalFeatures={{ariaV7: true}}
            localeText={ptBR.components.MuiDataGrid.defaultProps.localeText}
            getRowId={(row) => row._id}
            getRowHeight={() => 'auto'}
            disableDensitySelector
            slots={{toolbar: GridToolbar}}
            slotProps={{
              toolbar: {
                // csvOptions: { disableToolbarButton: true },
                // printOptions: { disableToolbarButton: true },
                showQuickFilter: true,
                quickFilterProps: {debounceMs: 250},
              },
            }}
            rows={items}
            columns={columns}
            className={styles.itemstable}
            // autoPageSize
            sx={{
              ".MuiTablePagination-root": {
                color: "red",
              },
            }}
        />
      </Container>
  )
}


export {ItemsTable};