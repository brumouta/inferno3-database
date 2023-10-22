import {ItemsTable} from "@/components/ItemsTable";
import {get} from "@/lib/api";
import {Item} from "@/types/item";


export default async function Home() {
  const res = await get<Item[]>(`${process.env.BACKEND_URL}/v1/items`);

  return (
    <ItemsTable items={res.data} ></ItemsTable>
  );
}
