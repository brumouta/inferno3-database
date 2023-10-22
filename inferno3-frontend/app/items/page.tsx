'use client'
import {ItemsTable} from "@/components/ItemsTable";
import {get} from "@/lib/api";
import {Item} from "@/types/item";
import {useSearchParams} from "next/navigation";


export default async function Items() {
  const searchParams = useSearchParams()!

  const res = await get<Item[]>(
      `${process.env.BACKEND_URL}/v1/items`
  );

  const quickFilter: string = searchParams && searchParams.get('area') ? searchParams.get('area')! : "";

  return (
    <ItemsTable items={res.data} quickFilter={quickFilter} ></ItemsTable>
  );
}
