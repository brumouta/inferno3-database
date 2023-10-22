import {get} from "@/lib/api";
import {Item} from "@/types/item";
import {ItemsTable} from "@/components/ItemsTable";


export default async function Infernais() {
  const res = await get<Item[]>(
      `${process.env.BACKEND_URL}/v1/items/infernais`
  );

  return (
    <ItemsTable items={res.data} quickFilter="Mercado Real" ></ItemsTable>
  );
}