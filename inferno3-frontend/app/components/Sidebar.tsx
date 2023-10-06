import {Stack, Typography} from "@mui/material";

function Sidebar() {
  return (
      <Stack direction="column" justifyContent="space-between">
        <Stack gap="8px">
          <Typography
              fontSize="13px"
              fontWeight="700"
              lineHeight="170%"
              sx={{ color: 'var(--colour-gray-400)' }}
          >
            Menu
          </Typography>
          {/*<TreeMenuList entries={filteredMenuConfiguration} level={0} />*/}
        </Stack>
      </Stack>
  );
};

export default Sidebar;
