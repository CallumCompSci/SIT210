using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;
using MyProject.Models;

namespace MyProject.Contexts;

public partial class DatabaseContext : DbContext
{
    public DatabaseContext()
    {
    }

    public DatabaseContext(DbContextOptions<DatabaseContext> options)
        : base(options)
    {
    }

    public virtual DbSet<Employee> Employees { get; set; }

    public virtual DbSet<Entry> Entries { get; set; }

    public virtual DbSet<Systemuser> Systemusers { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Employee>(entity =>
        {
            entity.HasKey(e => e.Id).HasName("employees_pkey");

            entity.ToTable("employees");

            entity.Property(e => e.Id)
                .UseIdentityAlwaysColumn()
                .HasColumnName("id");
            entity.Property(e => e.Createddate)
                .HasColumnType("timestamp without time zone")
                .HasColumnName("createddate");
            entity.Property(e => e.Dob).HasColumnName("dob");
            entity.Property(e => e.Fname)
                .HasMaxLength(50)
                .HasColumnName("fname");
            entity.Property(e => e.Lname)
                .HasMaxLength(50)
                .HasColumnName("lname");
            entity.Property(e => e.Modifieddate)
                .HasColumnType("timestamp without time zone")
                .HasColumnName("modifieddate");
            entity.Property(e => e.Photo).HasColumnName("photo");
        });

        modelBuilder.Entity<Entry>(entity =>
        {
            entity.HasKey(e => e.Entrynum).HasName("entries_pkey");

            entity.ToTable("entries");

            entity.Property(e => e.Entrynum)
                .UseIdentityAlwaysColumn()
                .HasColumnName("entrynum");
            entity.Property(e => e.Comment)
                .HasMaxLength(500)
                .HasColumnName("comment");
            entity.Property(e => e.Employeeid).HasColumnName("employeeid");
            entity.Property(e => e.Entrytime)
                .HasColumnType("timestamp without time zone")
                .HasColumnName("entrytime");
            entity.Property(e => e.Manualentry).HasColumnName("manualentry");
            entity.Property(e => e.Sysuserid).HasColumnName("sysuserid");
        });

        modelBuilder.Entity<Systemuser>(entity =>
        {
            entity.HasKey(e => e.SysId).HasName("systemusers_pkey");

            entity.ToTable("systemusers");

            entity.Property(e => e.SysId)
                .ValueGeneratedNever()
                .HasColumnName("sys_id");
            entity.Property(e => e.Createddate)
                .HasColumnType("timestamp without time zone")
                .HasColumnName("createddate");
            entity.Property(e => e.Isadmin).HasColumnName("isadmin");
            entity.Property(e => e.Modifieddate)
                .HasColumnType("timestamp without time zone")
                .HasColumnName("modifieddate");
            entity.Property(e => e.Passwordhash)
                .HasMaxLength(500)
                .HasColumnName("passwordhash");
        });

        OnModelCreatingPartial(modelBuilder);
    }

    partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
}
