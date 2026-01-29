--
-- PostgreSQL database dump
--

\restrict DLAzahWRoGVQizfRSHGq6gtI0oRKFFRQgieTr5GURSVoPtcQ0qdktmU6Ynj4CzR

-- Dumped from database version 15.15 (Debian 15.15-1.pgdg13+1)
-- Dumped by pg_dump version 15.15 (Debian 15.15-1.pgdg13+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: plan; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.plan (
    code character varying NOT NULL,
    name character varying NOT NULL,
    price integer NOT NULL,
    billing_cycle character varying NOT NULL,
    is_active boolean NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.plan OWNER TO "user";

--
-- Name: plan_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.plan_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.plan_id_seq OWNER TO "user";

--
-- Name: plan_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.plan_id_seq OWNED BY public.plan.id;


--
-- Name: planfeature; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.planfeature (
    key character varying NOT NULL,
    value character varying NOT NULL,
    id integer NOT NULL,
    plan_id integer NOT NULL
);


ALTER TABLE public.planfeature OWNER TO "user";

--
-- Name: planfeature_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.planfeature_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.planfeature_id_seq OWNER TO "user";

--
-- Name: planfeature_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.planfeature_id_seq OWNED BY public.planfeature.id;


--
-- Name: subscription; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.subscription (
    status character varying NOT NULL,
    starts_at timestamp without time zone NOT NULL,
    ends_at timestamp without time zone,
    id integer NOT NULL,
    user_id integer NOT NULL,
    plan_id integer NOT NULL
);


ALTER TABLE public.subscription OWNER TO "user";

--
-- Name: subscription_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.subscription_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.subscription_id_seq OWNER TO "user";

--
-- Name: subscription_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.subscription_id_seq OWNED BY public.subscription.id;


--
-- Name: translation_logs_detail; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.translation_logs_detail (
    id integer NOT NULL,
    user_id integer,
    action character varying(50) NOT NULL,
    engine character varying(20) NOT NULL,
    text_hash character varying(64) NOT NULL,
    char_count integer NOT NULL,
    context character varying(50),
    latency_ms integer,
    created_at timestamp without time zone NOT NULL
);


ALTER TABLE public.translation_logs_detail OWNER TO "user";

--
-- Name: translation_logs_detail_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.translation_logs_detail_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.translation_logs_detail_id_seq OWNER TO "user";

--
-- Name: translation_logs_detail_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.translation_logs_detail_id_seq OWNED BY public.translation_logs_detail.id;


--
-- Name: translation_phrases; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.translation_phrases (
    id integer NOT NULL,
    source_lang character varying(10) NOT NULL,
    target_lang character varying(10) NOT NULL,
    source_text character varying(255) NOT NULL,
    translated_text character varying(255) NOT NULL,
    context character varying(50),
    priority integer NOT NULL,
    created_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);


ALTER TABLE public.translation_phrases OWNER TO "user";

--
-- Name: translation_phrases_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.translation_phrases_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.translation_phrases_id_seq OWNER TO "user";

--
-- Name: translation_phrases_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.translation_phrases_id_seq OWNED BY public.translation_phrases.id;


--
-- Name: usagelog; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.usagelog (
    id integer NOT NULL,
    user_id integer NOT NULL,
    feature_key character varying NOT NULL,
    count integer NOT NULL,
    date character varying NOT NULL
);


ALTER TABLE public.usagelog OWNER TO "user";

--
-- Name: usagelog_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.usagelog_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.usagelog_id_seq OWNER TO "user";

--
-- Name: usagelog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.usagelog_id_seq OWNED BY public.usagelog.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public."user" (
    email character varying NOT NULL,
    name character varying,
    role character varying NOT NULL,
    phone character varying,
    id integer NOT NULL,
    hashed_password character varying NOT NULL,
    created_at timestamp without time zone NOT NULL
);


ALTER TABLE public."user" OWNER TO "user";

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO "user";

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: usersession; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.usersession (
    id integer NOT NULL,
    user_id integer NOT NULL,
    token_jti character varying NOT NULL,
    ip_address character varying,
    user_agent character varying,
    is_active boolean NOT NULL,
    created_at timestamp without time zone NOT NULL,
    last_active_at timestamp without time zone NOT NULL
);


ALTER TABLE public.usersession OWNER TO "user";

--
-- Name: usersession_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.usersession_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.usersession_id_seq OWNER TO "user";

--
-- Name: usersession_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.usersession_id_seq OWNED BY public.usersession.id;


--
-- Name: plan id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.plan ALTER COLUMN id SET DEFAULT nextval('public.plan_id_seq'::regclass);


--
-- Name: planfeature id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.planfeature ALTER COLUMN id SET DEFAULT nextval('public.planfeature_id_seq'::regclass);


--
-- Name: subscription id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.subscription ALTER COLUMN id SET DEFAULT nextval('public.subscription_id_seq'::regclass);


--
-- Name: translation_logs_detail id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.translation_logs_detail ALTER COLUMN id SET DEFAULT nextval('public.translation_logs_detail_id_seq'::regclass);


--
-- Name: translation_phrases id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.translation_phrases ALTER COLUMN id SET DEFAULT nextval('public.translation_phrases_id_seq'::regclass);


--
-- Name: usagelog id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.usagelog ALTER COLUMN id SET DEFAULT nextval('public.usagelog_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Name: usersession id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.usersession ALTER COLUMN id SET DEFAULT nextval('public.usersession_id_seq'::regclass);


--
-- Data for Name: plan; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.plan (code, name, price, billing_cycle, is_active, id) FROM stdin;
\.


--
-- Data for Name: planfeature; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.planfeature (key, value, id, plan_id) FROM stdin;
\.


--
-- Data for Name: subscription; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.subscription (status, starts_at, ends_at, id, user_id, plan_id) FROM stdin;
\.


--
-- Data for Name: translation_logs_detail; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.translation_logs_detail (id, user_id, action, engine, text_hash, char_count, context, latency_ms, created_at) FROM stdin;
\.


--
-- Data for Name: translation_phrases; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.translation_phrases (id, source_lang, target_lang, source_text, translated_text, context, priority, created_at, updated_at) FROM stdin;
\.


--
-- Data for Name: usagelog; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.usagelog (id, user_id, feature_key, count, date) FROM stdin;
\.


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public."user" (email, name, role, phone, id, hashed_password, created_at) FROM stdin;
vu.nguyen8182@gmail.com	Nguyễn An Vũ	user	\N	1	$argon2id$v=19$m=65536,t=3,p=4$BCCkFIIwRui9NyZE6L13Tg$OOY4StUpKf9vEFOBQfcuewO/9QVecbFRrn9o6nqaVTA	2026-01-29 08:51:50.730226
\.


--
-- Data for Name: usersession; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.usersession (id, user_id, token_jti, ip_address, user_agent, is_active, created_at, last_active_at) FROM stdin;
3	1	4c1d50ee-4049-4705-9e17-ffddae3452d5	10.200.1.129	Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36	t	2026-01-29 09:28:19.041315	2026-01-29 09:28:19.041325
\.


--
-- Name: plan_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.plan_id_seq', 1, false);


--
-- Name: planfeature_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.planfeature_id_seq', 1, false);


--
-- Name: subscription_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.subscription_id_seq', 1, false);


--
-- Name: translation_logs_detail_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.translation_logs_detail_id_seq', 1, false);


--
-- Name: translation_phrases_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.translation_phrases_id_seq', 1, false);


--
-- Name: usagelog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.usagelog_id_seq', 1, false);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.user_id_seq', 1, true);


--
-- Name: usersession_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.usersession_id_seq', 3, true);


--
-- Name: plan plan_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.plan
    ADD CONSTRAINT plan_pkey PRIMARY KEY (id);


--
-- Name: planfeature planfeature_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.planfeature
    ADD CONSTRAINT planfeature_pkey PRIMARY KEY (id);


--
-- Name: subscription subscription_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.subscription
    ADD CONSTRAINT subscription_pkey PRIMARY KEY (id);


--
-- Name: translation_logs_detail translation_logs_detail_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.translation_logs_detail
    ADD CONSTRAINT translation_logs_detail_pkey PRIMARY KEY (id);


--
-- Name: translation_phrases translation_phrases_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.translation_phrases
    ADD CONSTRAINT translation_phrases_pkey PRIMARY KEY (id);


--
-- Name: usagelog usagelog_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.usagelog
    ADD CONSTRAINT usagelog_pkey PRIMARY KEY (id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: usersession usersession_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.usersession
    ADD CONSTRAINT usersession_pkey PRIMARY KEY (id);


--
-- Name: ix_plan_code; Type: INDEX; Schema: public; Owner: user
--

CREATE UNIQUE INDEX ix_plan_code ON public.plan USING btree (code);


--
-- Name: ix_translation_logs_detail_text_hash; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX ix_translation_logs_detail_text_hash ON public.translation_logs_detail USING btree (text_hash);


--
-- Name: ix_translation_phrases_source_lang; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX ix_translation_phrases_source_lang ON public.translation_phrases USING btree (source_lang);


--
-- Name: ix_translation_phrases_source_text; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX ix_translation_phrases_source_text ON public.translation_phrases USING btree (source_text);


--
-- Name: ix_translation_phrases_target_lang; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX ix_translation_phrases_target_lang ON public.translation_phrases USING btree (target_lang);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: user
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: ix_usersession_token_jti; Type: INDEX; Schema: public; Owner: user
--

CREATE UNIQUE INDEX ix_usersession_token_jti ON public.usersession USING btree (token_jti);


--
-- Name: planfeature planfeature_plan_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.planfeature
    ADD CONSTRAINT planfeature_plan_id_fkey FOREIGN KEY (plan_id) REFERENCES public.plan(id);


--
-- Name: subscription subscription_plan_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.subscription
    ADD CONSTRAINT subscription_plan_id_fkey FOREIGN KEY (plan_id) REFERENCES public.plan(id);


--
-- Name: subscription subscription_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.subscription
    ADD CONSTRAINT subscription_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- Name: translation_logs_detail translation_logs_detail_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.translation_logs_detail
    ADD CONSTRAINT translation_logs_detail_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- Name: usagelog usagelog_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.usagelog
    ADD CONSTRAINT usagelog_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- Name: usersession usersession_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.usersession
    ADD CONSTRAINT usersession_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- PostgreSQL database dump complete
--

\unrestrict DLAzahWRoGVQizfRSHGq6gtI0oRKFFRQgieTr5GURSVoPtcQ0qdktmU6Ynj4CzR

