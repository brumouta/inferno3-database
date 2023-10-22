import {ItemsTable} from "@/components/ItemsTable";
import {get} from "@/lib/api";
import {Item} from "@/types/item";


export default async function Items({searchParams}: {searchParams: { area: string }}) {

  const res = await get<Item[]>(
      `${process.env.BACKEND_URL}/v1/items`
  );

  const quickFilter = searchParams && searchParams.area ? searchParams.area : "";

  return (
    <ItemsTable items={res.data} quickFilter={quickFilter} ></ItemsTable>
  );
}
