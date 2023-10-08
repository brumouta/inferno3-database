import {InfernaisTable} from "@/components/InfernaisTable";
import {get} from "@/lib/api";
import {Item} from "@/types/item";


export default async function Infernais() {
  const res = await get<Item[]>(`${process.env.BACKEND_URL}/v1/items/infernais`);

  return (
      <main>
        <InfernaisTable items={res.data} ></InfernaisTable>
      </main>
  );
}