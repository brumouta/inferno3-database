export interface Item {
  name: string | undefined;
  type: string | undefined;
  level: number | undefined;
  remort: number | undefined;
  value: number | undefined;
  weight: number | undefined;
  armor: number | undefined;
  abilities: string[] | undefined;
  properties: string[] | undefined;
  effects: object | undefined;
  prevents: string[] | undefined;
  capacity: string | undefined;
  wand: string | undefined;
  mob: string | undefined;
}