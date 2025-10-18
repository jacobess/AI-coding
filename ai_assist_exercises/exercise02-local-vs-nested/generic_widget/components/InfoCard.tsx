import React from "react";

type InfoCardProps = {
  title: string;
  message: string;
};

export function InfoCard({ title, message }: InfoCardProps) {
  return (
    <section className="rounded border border-slate-300 bg-white p-4 shadow-sm">
      <h2 className="text-lg font-semibold text-slate-800">{title}</h2>
      <p className="mt-1 text-sm text-slate-600">{message}</p>
    </section>
  );
}
