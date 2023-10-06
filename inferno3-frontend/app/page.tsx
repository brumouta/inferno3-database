import {ItemsTable} from "@/app/components/ItemsTable";
import {get} from "./lib/api";
import {Item} from "./types/item";


export default async function Home() {
  const res = await get<Item[]>(`${process.env.BACKEND_URL}/v1/items`);

  return (
      <main>
        <ItemsTable items={res.data} ></ItemsTable>
      </main>
  );
}
