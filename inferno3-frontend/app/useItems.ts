import {Item} from "@/app/types/item";

export async function getItems() : Promise<Item[]> {
  const res = await fetch(`${process.env.BACKEND_URL}/v1/items`)
  return await res.json()
}