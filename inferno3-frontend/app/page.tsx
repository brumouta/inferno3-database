import {ItemsTable} from "@/app/components/ItemsTable";
import {Item} from "@/app/types/item";
import {getItems} from "@/app/useItems";


export default async function Home() {
  const items: Item[] = await getItems()
  return (
      <main>
        <ItemsTable items={items} ></ItemsTable>
      </main>
  );
}
