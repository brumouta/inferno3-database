FROM node:18-alpine AS Base
ENV NODE_ENV=production
RUN apk add --no-cache libc6-compat
WORKDIR /app
COPY package.json pnpm-lock.yaml ./
RUN corepack enable && corepack prepare pnpm@latest --activate
RUN pnpm install --force

FROM node:18-alpine AS Builder
COPY .env ./
ARG BACKEND_URL
ENV BACKEND_URL $BACKEND_URL
ENV NODE_ENV=production
WORKDIR /app

COPY --from=Base /app/node_modules ./node_modules
COPY next.config.js ./
COPY package.json pnpm-lock.yaml ./
COPY tsconfig.json ./
COPY app ./app
COPY public ./public
RUN corepack enable && corepack prepare pnpm@latest --activate
RUN pnpm install --production
RUN pnpm run build

FROM node:18-alpine AS Runner
ENV NODE_ENV=production
WORKDIR /app

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=Builder /app/public ./public
COPY --from=Builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=Builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

CMD ["node", "server.js"]

#FROM oven/bun
#WORKDIR /app
#COPY package.json package.json
##COPY bun.lockb bun.lockb
#RUN bun install
#COPY app .
#COPY package.json .
#COPY tsconfig.json .
#COPY next.config.js .
#COPY next-env.d.ts .
#EXPOSE 3000
#ENTRYPOINT ["bun", "index.js"]
