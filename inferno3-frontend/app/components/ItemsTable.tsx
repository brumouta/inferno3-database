'use client'
import {Container} from "@mui/material";
import {DataGrid, GridColDef, GridToolbar, ptBR} from "@mui/x-data-grid";
import styles from './styles.module.css'
import {Item} from "@/app/types/item";

const formatArray = (params: any) => {
  return String(params.value).replaceAll(',', '\n');
};
const cons = (params: any) => {
  console.log(params);
  return params.value;
};

const columns: GridColDef[] = [
  { field: 'name', headerName: 'Nome', width: 300 },
  { field: 'type', headerName: 'Tipo', width: 100 },
  { field: 'level', headerName: 'Level', width: 80 },
  { field: 'remort', headerName: 'Remort', width: 100 },
  { field: 'value', headerName: 'Valor', width: 100 },
  { field: 'weight', headerName: 'Peso', width: 80 },
  { field: 'armor', headerName: 'Armadura', width: 120 },
  { field: 'abilities', headerName: 'Habilidades', width: 150, valueFormatter: formatArray },
  { field: 'properties', headerName: 'Propriedades', width: 150, valueFormatter: formatArray },
  { field: 'effects', headerName: 'Afetamentos', width: 100, valueFormatter: cons},
  { field: 'prevents', headerName: 'Prevenir', width: 100 },
  { field: 'capacity', headerName: 'Capacidade', width: 100 },
  { field: 'wand', headerName: 'Varinha', width: 100 },
  { field: 'mob', headerName: 'Mob', width: 100 },
];


interface Props {
  items: Item[];
}

const ItemsTable = ({ items }: Props) => {
  return (
      <Container>
        <DataGrid experimentalFeatures={{ariaV7: true}}
                  localeText={ptBR.components.MuiDataGrid.defaultProps.localeText}
                  getRowId={(row) => row._id}
                  getRowHeight={() => 'auto'}
                  slots={{ toolbar: GridToolbar }}
                  rows={items}
                  columns={columns}
                  className={styles.itemstable}
                  autoPageSize
                  sx={{
                    ".MuiTablePagination-root": {
                      color: "red",
                    },
                  }}
        />
      </Container>
  )
}


export { ItemsTable };