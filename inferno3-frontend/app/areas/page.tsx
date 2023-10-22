import {get} from "@/lib/api";
import {Link, List, ListItem, ListItemText} from "@mui/material";
import * as React from "react";


export default async function Areas() {
  const res = await get<string[]>(
      `${process.env.BACKEND_URL}/v1/areas`
  );

  return (
      <List dense>
        {res.data.map((area) => (
            <ListItem key={area}>
              <Link
                  underline={"none"}
                  // sx={{ my: 2, color: 'red', display: 'block', font: "monospace" }}
                  href={`/items?area=${area}`}
              >
                <ListItemText primary={area} />
              </Link>
            </ListItem>
        ))}
      </List>
  );
}