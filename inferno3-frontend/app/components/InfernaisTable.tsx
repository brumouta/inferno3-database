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
  { field: 'name', headerName: 'Nome', width: 300 },
  { field: 'type', headerName: 'Tipo', width: 100 },
  { field: 'level', headerName: 'Level', width: 80 },
  { field: 'remort', headerName: 'Remort', width: 100 },
  { field: 'value', headerName: 'Valor', width: 100 },
  { field: 'dice', headerName: 'Dado de Dano', width: 80 },
  { field: 'damage', headerName: 'Dano médio', width: 80 },
  { field: 'weight', headerName: 'Peso', width: 80 },
  { field: 'armor', headerName: 'Armadura', width: 120 },
  { field: 'slot', headerName: 'Local', width: 120 },
  { field: 'abilities', headerName: 'Habilidades', width: 130, valueFormatter: formatArray },
  { field: 'properties', headerName: 'Propriedades', width: 150, valueFormatter: formatArray },
  { field: 'effects', headerName: 'Afetamentos', width: 130, valueFormatter: formatEffects},
  { field: 'prevents', headerName: 'Prevenir', width: 120 },
  { field: 'seller', headerName: 'Vendedor', width: 100 },
  { field: 'price', headerName: 'Preço', width: 100 },
  { field: 'room', headerName: 'Sala', width: 100 },
  { field: 'area', headerName: 'Área', width: 100 },
];


interface Props {
  items: Item[];
}

const InfernaisTable = ({ items }: Props) => {
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


export { InfernaisTable };